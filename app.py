import os
import json
import re
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
from typing import List, Dict, Any
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = FastAPI()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, Any]]

@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/chat_stream")
def chat_stream_endpoint(req: ChatRequest):
    """
    Standard Chat Stream. Detects [[START_RESEARCH]] tag.
    """
    
    formatted_input = []
    for msg in req.history:
        if msg.get("role") in ["user", "model"]:
            formatted_input.append({
                "role": msg["role"],
                "content": [{"type": "text", "text": msg["text"]}]
            })
            
    formatted_input.append({
        "role": "user",
        "content": [{"type": "text", "text": req.message}]
    })

    sys_instruction = (
        "You are a Senior Principal Researcher. Your goal: refine a vague user idea into a concrete, novel research hypothesis.\n"
        "1. Use Google Search to check the frontier of the field.\n"
        "2. Discuss with the user until the hypothesis is specific and novel.\n"
        "3. CRITICAL: When (and only when) the user agrees to a solid hypothesis, you must output a special trigger command.\n"
        "   The format is: [[START_RESEARCH: <insert_detailed_topic_here>]]\n"
        "   Example: [[START_RESEARCH: The impact of transformer architecture on proactive resource allocation in edge computing]]\n"
        "   Do not write anything else after this tag."
    )

    def event_generator():
        try:
            stream = client.interactions.create(
                model="gemini-3-flash-preview", 
                input=formatted_input,
                tools=[{"type": "google_search"}], 
                system_instruction=sys_instruction,
                generation_config={"thinking_level": "high", "thinking_summaries": "auto"},
                stream=True
            )

            buffer = ""
            for chunk in stream:
                if chunk.event_type == "content.delta":
                    if chunk.delta.type == "thought" and chunk.delta.thought:
                        yield json.dumps({"type": "thought_delta", "content": chunk.delta.thought}) + "\n"
                    elif chunk.delta.type == "text" and chunk.delta.text:
                        buffer += chunk.delta.text
                        match = re.search(r"\[\[START_RESEARCH:\s*(.*?)\]\]", buffer)
                        if match:
                            topic = match.group(1).strip()
                            research_id = trigger_deep_research_agent(topic)
                            yield json.dumps({"type": "RESEARCH_STARTED", "topic": topic, "id": research_id}) + "\n"
                            return 
                        yield json.dumps({"type": "text", "content": chunk.delta.text}) + "\n"
        except Exception as e:
            yield json.dumps({"type": "error", "content": str(e)}) + "\n"

    return StreamingResponse(event_generator(), media_type="application/x-ndjson")

def trigger_deep_research_agent(topic: str):
    """Starts the Agent in background mode."""
    print(f"Starting Deep Research on: {topic}")
    prompt = f"Conduct deep research on: {topic}. 1. State of Art. 2. Novel Hypothesis. 3. Experiment Plan."
    interaction = client.interactions.create(
        agent="deep-research-pro-preview-12-2025",
        input=prompt,
        background=True
    )
    return interaction.id

@app.get("/api/research_stream/{interaction_id}")
def research_stream_endpoint(interaction_id: str):
    """
    Proxies the Deep Research Agent's live events to the UI.
    """
    def event_generator():
        try:
            # Resume the stream from the background interaction
            stream = client.interactions.get(id=interaction_id, stream=True)
            
            for chunk in stream:
                event_type = chunk.event_type
                
                # 1. Thought Process (Reasoning)
                if event_type == "content.delta":
                    if chunk.delta.type == "thought" and chunk.delta.thought:
                         yield json.dumps({"type": "log", "category": "thinking", "content": chunk.delta.thought}) + "\n"
                    
                    # 2. Search / Tool Calls
                    # Note: The SDK maps specific tool calls differently based on version, 
                    # generic handling allows us to catch searches.
                    elif chunk.delta.type == "google_search_call":
                         # Extract query if available
                         query = "Searching Google..."
                         if hasattr(chunk.delta, 'arguments') and 'queries' in chunk.delta.arguments:
                             query = f"Searching: {chunk.delta.arguments['queries']}"
                         yield json.dumps({"type": "log", "category": "search", "content": query}) + "\n"

                    elif chunk.delta.type == "url_context_call":
                         yield json.dumps({"type": "log", "category": "reading", "content": "Reading external sources..."}) + "\n"
                    
                    # 3. Final Report Drafting
                    elif chunk.delta.type == "text" and chunk.delta.text:
                         yield json.dumps({"type": "report_delta", "content": chunk.delta.text}) + "\n"

                # 4. Completion
                elif event_type == "interaction.complete":
                    yield json.dumps({"type": "complete"}) + "\n"
                    return

        except Exception as e:
            print(f"Research Stream Error: {e}")
            yield json.dumps({"type": "error", "content": str(e)}) + "\n"

    return StreamingResponse(event_generator(), media_type="application/x-ndjson")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)