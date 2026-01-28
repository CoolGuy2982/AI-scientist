The Gemini Interactions API is an experimental API that allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.  
[View as markdown](https://ai.google.dev/static/api/interactions.md.txt)[View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)  

## Creating an interaction

posthttps://generativelanguage.googleapis.com/v1beta/interactions
Creates a new interaction.
- [Request body](https://ai.google.dev/api/interactions-api#CreateInteraction.request_body)
- [Response](https://ai.google.dev/api/interactions-api#CreateInteraction.response)

### Request body

The request body contains data with the following structure:
modelModelOption(optional)  
The name of the \`Model\` used for generating the interaction.  
**Required if \`agent\` is not provided.**

Possible values:

- `gemini-2.5-pro`

  Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
- `gemini-2.5-flash`

  Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.
- `gemini-2.5-flash-preview-09-2025`

  The latest model based on the 2.5 Flash model. 2.5 Flash Preview is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.
- `gemini-2.5-flash-lite`

  Our smallest and most cost effective model, built for at scale usage.
- `gemini-2.5-flash-lite-preview-09-2025`

  The latest model based on Gemini 2.5 Flash lite optimized for cost-efficiency, high throughput and high quality.
- `gemini-2.5-flash-preview-native-audio-dialog`

  Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
- `gemini-2.5-flash-image-preview`

  Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.
- `gemini-2.5-pro-preview-tts`

  Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
- `gemini-3-pro-preview`

  Our most intelligent model with SOTA reasoning and multimodal understanding, and powerful agentic and vibe coding capabilities.
- `gemini-3-flash-preview`

  Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.
agentAgentOption(optional)  
The name of the \`Agent\` used for generating the interaction.  
**Required if \`model\` is not provided.**

Possible values:

- `deep-research-pro-preview-12-2025`

  Gemini Deep Research Agent

The agent to interact with.  
input[Content](https://ai.google.dev/api/interactions-api#Resource:Content)or array ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ([Turn](https://ai.google.dev/api/interactions-api#Resource:Turn)) or string(required)  
The inputs for the interaction (common to both Model and Agent).  
system_instructionstring(optional)  
System instruction for the interaction.  
toolsarray ([Tool](https://ai.google.dev/api/interactions-api#Resource:Tool))(optional)  
A list of tool declarations the model may call during interaction.  
response_formatobject(optional)  
Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.  
response_mime_typestring(optional)  
The mime type of the response. This is required if response_format is set.  
streamboolean(optional)  
Input only. Whether the interaction will be streamed.  
storeboolean(optional)  
Input only. Whether to store the response and request for later retrieval.  
backgroundboolean(optional)  
Whether to run the model interaction in the background.
generation_configGenerationConfig(optional)  
**Model Configuration**   
Configuration parameters for the model interaction.  
*Alternative to \`agent_config\`. Only applicable when \`model\` is set.*
Configuration parameters for model interactions.

#### Fields

temperaturenumber(optional)  
Controls the randomness of the output.  
top_pnumber(optional)  
The maximum cumulative probability of tokens to consider when sampling.  
seedinteger(optional)  
Seed used in decoding for reproducibility.  
stop_sequencesarray (string)(optional)  
A list of character sequences that will stop output interaction.
tool_choiceToolChoice(optional)  
The tool choice for the interaction.
The configuration for tool choice.

#### Possible Types

ToolChoiceType  
<br />

This type has no specific fields.
ToolChoiceConfig  
<br />

allowed_toolsAllowedTools(optional)  
No description provided.
The configuration for allowed tools.

#### Fields

modeToolChoiceType(optional)  
The mode of the tool choice.

Possible values:

- `auto`
- `any`
- `none`
- `validated`

<br />

toolsarray (string)(optional)  
The names of the allowed tools.
thinking_levelThinkingLevel(optional)  
The level of thought tokens that the model should generate.

Possible values:

- `minimal`
- `low`
- `medium`
- `high`

<br />

thinking_summariesThinkingSummaries(optional)  
Whether to include thought summaries in the response.

Possible values:

- `auto`
- `none`

<br />

max_output_tokensinteger(optional)  
The maximum number of tokens to include in the response.
speech_configSpeechConfig(optional)  
Configuration for speech interaction.
The configuration for speech interaction.

#### Fields

voicestring(optional)  
The voice of the speaker.  
languagestring(optional)  
The language of the speech.  
speakerstring(optional)  
The speaker's name, it should match the speaker name given in the prompt.
agent_configobject(optional)  
**Agent Configuration**   
Configuration for the agent.  
*Alternative to \`generation_config\`. Only applicable when \`agent\` is set.*

#### Possible Types

Polymorphic discriminator:`type`
DynamicAgentConfig  
Configuration for dynamic agents.  
typeobject(optional)  
No description provided.

Always set to`"dynamic"`.
DeepResearchAgentConfig  
Configuration for the Deep Research agent.
thinking_summariesThinkingSummaries(optional)  
Whether to include thought summaries in the response.

Possible values:

- `auto`
- `none`

<br />

typeobject(optional)  
No description provided.

Always set to`"deep-research"`.
response_modalitiesResponseModality(optional)  
The requested modalities of the response (TEXT, IMAGE, AUDIO).

Possible values:

- `text`
- `image`
- `audio`

<br />

previous_interaction_idstring(optional)  
The ID of the previous interaction, if any.

### Response

Returns an[Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)resource.  

### Simple Request

#### Example Response

```json
{
  "created": "2025-11-26T12:25:15Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-2.5-flash",
  "object": "interaction",
  "outputs": [
    {
      "text": "Hello! I'm functioning perfectly and ready to assist you.\n\nHow are you doing today?",
      "type": "text"
    }
  ],
  "role": "model",
  "status": "completed",
  "updated": "2025-11-26T12:25:15Z",
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 7
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 20,
    "total_reasoning_tokens": 22,
    "total_tokens": 49,
    "total_tool_use_tokens": 0
  }
}
```

### Multi-turn

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-2.5-flash",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "The capital of France is Paris."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 50
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 50,
    "total_output_tokens": 10,
    "total_reasoning_tokens": 0,
    "total_tokens": 60,
    "total_tool_use_tokens": 0
  }
}
```

### Image Input

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-2.5-flash",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "A white humanoid robot with glowing blue eyes stands holding a red skateboard."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 10
      },
      {
        "modality": "image",
        "tokens": 258
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 268,
    "total_output_tokens": 20,
    "total_reasoning_tokens": 0,
    "total_tokens": 288,
    "total_tool_use_tokens": 0
  }
}
```

### Function Calling

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-2.5-flash",
  "status": "requires_action",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "function_call",
      "function_call": {
        "name": "get_weather",
        "arguments": {
          "location": "Boston, MA"
        }
      }
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 100
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 100,
    "total_output_tokens": 25,
    "total_reasoning_tokens": 0,
    "total_tokens": 125,
    "total_tool_use_tokens": 50
  }
}
```

### Deep Research

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "agent": "deep-research-pro-preview-12-2025",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Here is a comprehensive research report on the current state of cancer research..."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 20
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 20,
    "total_output_tokens": 1000,
    "total_reasoning_tokens": 500,
    "total_tokens": 1520,
    "total_tool_use_tokens": 0
  }
}
```  

## Retrieving an interaction

gethttps://generativelanguage.googleapis.com/v1beta/interactions/{id}
Retrieves the full details of a single interaction based on its \`Interaction.id\`.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#getInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#getInteractionById.response)

### Path / Query Parameters

idstring(required)  
The unique identifier of the interaction to retrieve.  
streamboolean(optional)  
If set to true, the generated content will be streamed incrementally.

*Defaults to:`False`*  
last_event_idstring(optional)  
Optional. If set, resumes the interaction stream from the next chunk after the event marked by the event id. Can only be used if \`stream\` is true.  
api_versionstring(optional)  
Which version of the API to use.

### Response

Returns an[Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)resource.  

### Get Interaction

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-2.5-flash",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:25:15Z",
  "updated": "2025-11-26T12:25:15Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "I'm doing great, thank you for asking! How can I help you today?"
    }
  ]
}
```  

## Deleting an interaction

deletehttps://generativelanguage.googleapis.com/v1beta/interactions/{id}
Deletes the interaction by id.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#deleteInteraction.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#deleteInteraction.response)

### Path / Query Parameters

idstring(required)  
The unique identifier of the interaction to delete.  
api_versionstring(optional)  
Which version of the API to use.

### Response

If successful, the response is empty.  

### Delete Interaction

## Canceling an interaction

posthttps://generativelanguage.googleapis.com/v1beta/interactions/{id}/cancel
Cancels an interaction by id. This only applies to background interactions that are still running.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#cancelInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#cancelInteractionById.response)

### Path / Query Parameters

idstring(required)  
The unique identifier of the interaction to cancel.  
api_versionstring(optional)  
Which version of the API to use.

### Response

Returns an[Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)resource.  

### Cancel Interaction

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "agent": "deep-research-pro-preview-12-2025",
  "status": "cancelled",
  "object": "interaction",
  "created": "2025-11-26T12:25:15Z",
  "updated": "2025-11-26T12:25:15Z",
  "role": "model"
}
```

## Resources

### Interaction

The Interaction resource.

#### Fields

modelModelOption(optional)  
The name of the \`Model\` used for generating the interaction.

Possible values:

- `gemini-2.5-pro`

  Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
- `gemini-2.5-flash`

  Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.
- `gemini-2.5-flash-preview-09-2025`

  The latest model based on the 2.5 Flash model. 2.5 Flash Preview is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.
- `gemini-2.5-flash-lite`

  Our smallest and most cost effective model, built for at scale usage.
- `gemini-2.5-flash-lite-preview-09-2025`

  The latest model based on Gemini 2.5 Flash lite optimized for cost-efficiency, high throughput and high quality.
- `gemini-2.5-flash-preview-native-audio-dialog`

  Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
- `gemini-2.5-flash-image-preview`

  Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.
- `gemini-2.5-pro-preview-tts`

  Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
- `gemini-3-pro-preview`

  Our most intelligent model with SOTA reasoning and multimodal understanding, and powerful agentic and vibe coding capabilities.
- `gemini-3-flash-preview`

  Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.
agentAgentOption(optional)  
The name of the \`Agent\` used for generating the interaction.

Possible values:

- `deep-research-pro-preview-12-2025`

  Gemini Deep Research Agent

The agent to interact with.  
idstring(optional)  
Output only. A unique identifier for the interaction completion.  
statusenum (string)(optional)  
Output only. The status of the interaction.

Possible values:

- `in_progress`
- `requires_action`
- `completed`
- `failed`
- `cancelled`  
createdstring(optional)  
Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
updatedstring(optional)  
Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
rolestring(optional)  
Output only. The role of the interaction.  
outputsarray ([Content](https://ai.google.dev/api/interactions-api#Resource:Content))(optional)  
Output only. Responses from the model.  
objectstring(optional)  
Output only. The object type of the interaction. Always set to \`interaction\`.

Always set to`"interaction"`.
usageUsage(optional)  
Output only. Statistics on the interaction request's token usage.
Statistics on the interaction request's token usage.

#### Fields

total_input_tokensinteger(optional)  
Number of tokens in the prompt (context).
input_tokens_by_modalityModalityTokens(optional)  
A breakdown of input token usage by modality.
The token count for a single response modality.

#### Fields

modalityResponseModality(optional)  
The modality associated with the token count.

Possible values:

- `text`
- `image`
- `audio`

<br />

tokensinteger(optional)  
Number of tokens for the modality.  
total_cached_tokensinteger(optional)  
Number of tokens in the cached part of the prompt (the cached content).
cached_tokens_by_modalityModalityTokens(optional)  
A breakdown of cached token usage by modality.
The token count for a single response modality.

#### Fields

modalityResponseModality(optional)  
The modality associated with the token count.

Possible values:

- `text`
- `image`
- `audio`

<br />

tokensinteger(optional)  
Number of tokens for the modality.  
total_output_tokensinteger(optional)  
Total number of tokens across all the generated responses.
output_tokens_by_modalityModalityTokens(optional)  
A breakdown of output token usage by modality.
The token count for a single response modality.

#### Fields

modalityResponseModality(optional)  
The modality associated with the token count.

Possible values:

- `text`
- `image`
- `audio`

<br />

tokensinteger(optional)  
Number of tokens for the modality.  
total_tool_use_tokensinteger(optional)  
Number of tokens present in tool-use prompt(s).
tool_use_tokens_by_modalityModalityTokens(optional)  
A breakdown of tool-use token usage by modality.
The token count for a single response modality.

#### Fields

modalityResponseModality(optional)  
The modality associated with the token count.

Possible values:

- `text`
- `image`
- `audio`

<br />

tokensinteger(optional)  
Number of tokens for the modality.  
total_reasoning_tokensinteger(optional)  
Number of tokens of thoughts for thinking models.  
total_tokensinteger(optional)  
Total token count for the interaction request (prompt + responses + other internal tokens).  
previous_interaction_idstring(optional)  
The ID of the previous interaction, if any.  

### Examples

### Example

```bash
{
  "created": "2025-12-04T15:01:45Z",
  "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
  "model": "gemini-2.5-flash",
  "object": "interaction",
  "outputs": [
    {
      "text": "Hello! I'm doing well, functioning as expected. Thank you for asking! How are you doing today?",
      "type": "text"
    }
  ],
  "role": "model",
  "status": "completed",
  "updated": "2025-12-04T15:01:45Z",
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 7
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 23,
    "total_reasoning_tokens": 49,
    "total_tokens": 79,
    "total_tool_use_tokens": 0
  }
}
```

## Data Models

### Content

The content of the response.

### Possible Types

Polymorphic discriminator:`type`
TextContent  
A text content block.  
textstring(optional)  
The text content.
annotationsAnnotation(optional)  
Citation information for model-generated content.
Citation information for model-generated content.

#### Fields

start_indexinteger(optional)  
Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.  
end_indexinteger(optional)  
End of the attributed segment, exclusive.  
sourcestring(optional)  
Source attributed for a portion of the text. Could be a URL, title, or other identifier.  
typeobject(required)  
No description provided.

Always set to`"text"`.
ImageContent  
An image content block.  
datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeImageMimeTypeOption(optional)  
No description provided.

Possible values:

- `image/png`
- `image/jpeg`
- `image/webp`
- `image/heic`
- `image/heif`

The mime type of the image.
resolutionMediaResolution(optional)  
The resolution of the media.

Possible values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

typeobject(required)  
No description provided.

Always set to`"image"`.
AudioContent  
An audio content block.  
datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeAudioMimeTypeOption(optional)  
No description provided.

Possible values:

- `audio/wav`
- `audio/mp3`
- `audio/aiff`
- `audio/aac`
- `audio/ogg`
- `audio/flac`

The mime type of the audio.  
typeobject(required)  
No description provided.

Always set to`"audio"`.
DocumentContent  
A document content block.  
datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeDocumentMimeTypeOption(optional)  
No description provided.

Possible values:

- `application/pdf`

The mime type of the document.  
typeobject(required)  
No description provided.

Always set to`"document"`.
VideoContent  
A video content block.  
datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeVideoMimeTypeOption(optional)  
No description provided.

Possible values:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

The mime type of the video.
resolutionMediaResolution(optional)  
The resolution of the media.

Possible values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

typeobject(required)  
No description provided.

Always set to`"video"`.
ThoughtContent  
A thought content block.  
signaturestring(optional)  
Signature to match the backend source to be part of the generation.
summaryThoughtSummary(optional)  
A summary of the thought.
A summary of the thought.  
typeobject(required)  
No description provided.

Always set to`"thought"`.
FunctionCallContent  
A function tool call content block.  
namestring(required)  
The name of the tool to call.  
argumentsobject(required)  
The arguments to pass to the function.  
typeobject(required)  
No description provided.

Always set to`"function_call"`.  
idstring(required)  
A unique ID for this specific tool call.
FunctionResultContent  
A function tool result content block.  
namestring(optional)  
The name of the tool that was called.  
is_errorboolean(optional)  
Whether the tool call resulted in an error.  
typeobject(required)  
No description provided.

Always set to`"function_result"`.  
resultobject or string(required)  
The result of the tool call.  
call_idstring(required)  
ID to match the ID from the function call block.
CodeExecutionCallContent  
Code execution content.
argumentsCodeExecutionCallArguments(optional)  
The arguments to pass to the code execution.
The arguments to pass to the code execution.

#### Fields

languageenum (string)(optional)  
Programming language of the \`code\`.

Possible values:

- `python`  
codestring(optional)  
The code to be executed.  
typeobject(required)  
No description provided.

Always set to`"code_execution_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
CodeExecutionResultContent  
Code execution result content.  
resultstring(optional)  
The output of the code execution.  
is_errorboolean(optional)  
Whether the code execution resulted in an error.  
signaturestring(optional)  
A signature hash for backend validation.  
typeobject(required)  
No description provided.

Always set to`"code_execution_result"`.  
call_idstring(optional)  
ID to match the ID from the code execution call block.
UrlContextCallContent  
URL context content.
argumentsUrlContextCallArguments(optional)  
The arguments to pass to the URL context.
The arguments to pass to the URL context.

#### Fields

urlsarray (string)(optional)  
The URLs to fetch.  
typeobject(required)  
No description provided.

Always set to`"url_context_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
UrlContextResultContent  
URL context result content.  
signaturestring(optional)  
The signature of the URL context result.
resultUrlContextResult(optional)  
The results of the URL context.
The result of the URL context.

#### Fields

urlstring(optional)  
The URL that was fetched.  
statusenum (string)(optional)  
The status of the URL retrieval.

Possible values:

- `success`
- `error`
- `paywall`
- `unsafe`  
is_errorboolean(optional)  
Whether the URL context resulted in an error.  
typeobject(required)  
No description provided.

Always set to`"url_context_result"`.  
call_idstring(optional)  
ID to match the ID from the url context call block.
GoogleSearchCallContent  
Google Search content.
argumentsGoogleSearchCallArguments(optional)  
The arguments to pass to Google Search.
The arguments to pass to Google Search.

#### Fields

queriesarray (string)(optional)  
Web search queries for the following-up web search.  
typeobject(required)  
No description provided.

Always set to`"google_search_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
GoogleSearchResultContent  
Google Search result content.  
signaturestring(optional)  
The signature of the Google Search result.
resultGoogleSearchResult(optional)  
The results of the Google Search.
The result of the Google Search.

#### Fields

urlstring(optional)  
URI reference of the search result.  
titlestring(optional)  
Title of the search result.  
rendered_contentstring(optional)  
Web content snippet that can be embedded in a web page or an app webview.  
is_errorboolean(optional)  
Whether the Google Search resulted in an error.  
typeobject(required)  
No description provided.

Always set to`"google_search_result"`.  
call_idstring(optional)  
ID to match the ID from the google search call block.
McpServerToolCallContent  
MCPServer tool call content.  
namestring(required)  
The name of the tool which was called.  
server_namestring(required)  
The name of the used MCP server.  
argumentsobject(required)  
The JSON object of arguments for the function.  
typeobject(required)  
No description provided.

Always set to`"mcp_server_tool_call"`.  
idstring(required)  
A unique ID for this specific tool call.
McpServerToolResultContent  
MCPServer tool result content.  
namestring(optional)  
Name of the tool which is called for this specific tool call.  
server_namestring(optional)  
The name of the used MCP server.  
typeobject(required)  
No description provided.

Always set to`"mcp_server_tool_result"`.  
resultobject or string(required)  
The result of the tool call.  
call_idstring(required)  
ID to match the ID from the MCP server tool call block.
FileSearchResultContent  
File Search result content.
resultFileSearchResult(optional)  
The results of the File Search.
The result of the File Search.

#### Fields

titlestring(optional)  
The title of the search result.  
textstring(optional)  
The text of the search result.  
file_search_storestring(optional)  
The name of the file search store.  
typeobject(required)  
No description provided.

Always set to`"file_search_result"`.  

### Examples

### Text

```json
{
  "type": "text",
  "text": "Hello, how are you?"
}
```

### Image

```json
{
  "type": "image",
  "data": "BASE64_ENCODED_IMAGE",
  "mime_type": "image/png"
}
```

### Audio

```json
{
  "type": "audio",
  "data": "BASE64_ENCODED_AUDIO",
  "mime_type": "audio/wav"
}
```

### Document

```json
{
  "type": "document",
  "data": "BASE64_ENCODED_DOCUMENT",
  "mime_type": "application/pdf"
}
```

### Video

```json
{
  "type": "video",
  "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
}
```

### Thought

```json
{
  "type": "thought",
  "summary": [
    {
      "type": "text",
      "text": "The user is asking about the weather. I should use the get_weather tool."
    }
  ],
  "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0+19xcLsGG46bd8wjkF/6RNlRUdvHrXyjsHkG0BZFcuO/bPOyA6Xh5jANNgx82wPHjGExN8A4ZQn56FlMwyZoqFVQz0QyY1lfibFJ2zU3J87uw26OewzcuVX0KEcs+GIsZa3EA6WwqhbsOd3wtZB3Ua2Qf98VAWZTS5y/tWpql7jnU3/CU7pouxQr/Bwft3hwnJNesQ9/dDJTuaQ8Zprh9VRWf1aFFjpIueOjBRrlT3oW6/y/eRl/Gt9BQXCYTqg/38vHFUU4Wo/d9dUpvfCe/a3o97t2Jgxp34oFKcsVb4S5WJrykIkw+14DzVnTpCpbQNFckqvFLuqnJCkL0EQFtunBXI03FJpPu3T1XU6id8S7ojoJQZSauGUCgmaLqUGdMrd08oo81ecoJSLs51Re9N/lISGmjWFPGpqJLoGq6uo4FHz58hmeyXCgHG742BHz2P3MiH1CXHUT2J8mF6zLhf3SR9Qb3lkrobAh"
}
```

### Function Call

```json
{
  "type": "function_call",
  "name": "get_weather",
  "id": "gth23981",
  "arguments": {
    "location": "Boston, MA"
  }
}
```

### Function Result

```json
{
  "type": "function_result",
  "name": "get_weather",
  "call_id": "gth23981",
  "result": {
    "weather": "sunny"
  }
}
```

### Code Execution Call

```json
{
  "type": "code_execution_call",
  "id": "call_123456",
  "arguments": {
    "language": "python",
    "code": "print('hello world')"
  }
}
```

### Code Execution Result

```json
{
  "type": "code_execution_result",
  "call_id": "call_123456",
  "result": "hello world\n"
}
```

### Url Context Call

```json
{
  "type": "url_context_call",
  "id": "call_123456",
  "arguments": {
    "urls": [
      "https://www.example.com"
    ]
  }
}
```

### Url Context Result

```json
{
  "type": "url_context_result",
  "call_id": "call_123456",
  "result": [
    {
      "url": "https://www.example.com",
      "status": "SUCCESS"
    }
  ]
}
```

### Google Search Call

```json
{
  "type": "google_search_call",
  "id": "call_123456",
  "arguments": {
    "queries": [
      "weather in Boston"
    ]
  }
}
```

### Google Search Result

```json
{
  "type": "google_search_result",
  "call_id": "call_123456",
  "result": [
    {
      "url": "https://www.google.com/search?q=weather+in+Boston",
      "title": "Weather in Boston"
    }
  ]
}
```

### Mcp Server Tool Call

```json
{
  "type": "mcp_server_tool_call",
  "id": "call_123456",
  "name": "get_forecast",
  "server_name": "weather_server",
  "arguments": {
    "city": "London"
  }
}
```

### Mcp Server Tool Result

```json
{
  "type": "mcp_server_tool_result",
  "name": "get_forecast",
  "server_name": "weather_server",
  "call_id": "call_123456",
  "result": "sunny"
}
```

### File Search Result

```json
{
  "type": "file_search_result",
  "result": [
    {
      "text": "search result chunk",
      "file_search_store": "file_search_store"
    }
  ]
}
```  

### Tool

<br />

### Possible Types

Polymorphic discriminator:`type`
Function  
A tool that can be used by the model.  
namestring(optional)  
The name of the function.  
descriptionstring(optional)  
A description of the function.  
parametersobject(optional)  
The JSON Schema for the function's parameters.  
typestring(required)  
No description provided.

Always set to`"function"`.
GoogleSearch  
A tool that can be used by the model to search Google.  
typestring(required)  
No description provided.

Always set to`"google_search"`.
CodeExecution  
A tool that can be used by the model to execute code.  
typestring(required)  
No description provided.

Always set to`"code_execution"`.
UrlContext  
A tool that can be used by the model to fetch URL context.  
typestring(required)  
No description provided.

Always set to`"url_context"`.
ComputerUse  
A tool that can be used by the model to interact with the computer.  
environmentenum (string)(optional)  
The environment being operated.

Possible values:

- `browser`  
excludedPredefinedFunctionsarray (string)(optional)  
The list of predefined functions that are excluded from the model call.  
typestring(required)  
No description provided.

Always set to`"computer_use"`.
McpServer  
A MCPServer is a server that can be called by the model to perform actions.  
namestring(optional)  
The name of the MCPServer.  
urlstring(optional)  
The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"  
headersobject(optional)  
Optional: Fields for authentication headers, timeouts, etc., if needed.
allowed_toolsAllowedTools(optional)  
The allowed tools.
The configuration for allowed tools.

#### Fields

modeToolChoiceType(optional)  
The mode of the tool choice.

Possible values:

- `auto`
- `any`
- `none`
- `validated`

<br />

toolsarray (string)(optional)  
The names of the allowed tools.  
typestring(required)  
No description provided.

Always set to`"mcp_server"`.
FileSearch  
A tool that can be used by the model to search files.  
file_search_store_namesarray (string)(optional)  
The file search store names to search.  
top_kinteger(optional)  
The number of semantic retrieval chunks to retrieve.  
metadata_filterstring(optional)  
Metadata filter to apply to the semantic retrieval documents and chunks.  
typestring(required)  
No description provided.

Always set to`"file_search"`.  

### Examples

### Function

### GoogleSearch

### CodeExecution

### UrlContext

### ComputerUse

### McpServer

### FileSearch

### Turn

<br />

#### Fields

rolestring(optional)  
The originator of this turn. Must be user for input or model for model output.  
contentarray ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or string(optional)  
The content of the turn.  

### Examples

### User Turn

```bash
{
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": "user turn"
    }
  ]
}
```

### Model Turn

```bash
{
  "role": "model",
  "content": [
    {
      "type": "text",
      "text": "model turn"
    }
  ]
}
```  

### InteractionSseEvent

<br />

### Possible Types

Polymorphic discriminator:`event_type`
InteractionEvent  
<br />

event_typeenum (string)(optional)  
No description provided.

Possible values:

- `interaction.start`
- `interaction.complete`  
interaction[Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction)(optional)  
No description provided.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.
InteractionStatusUpdate  
<br />

interaction_idstring(optional)  
No description provided.  
statusenum (string)(optional)  
No description provided.

Possible values:

- `in_progress`
- `requires_action`
- `completed`
- `failed`
- `cancelled`  
event_typestring(optional)  
No description provided.

Always set to`"interaction.status_update"`.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.
ContentStart  
<br />

indexinteger(optional)  
No description provided.  
content[Content](https://ai.google.dev/api/interactions-api#Resource:Content)(optional)  
No description provided.  
event_typestring(optional)  
No description provided.

Always set to`"content.start"`.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.
ContentDelta  
<br />

indexinteger(optional)  
No description provided.  
event_typestring(optional)  
No description provided.

Always set to`"content.delta"`.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.
deltaobject(optional)  
No description provided.

#### Possible Types

Polymorphic discriminator:`type`
TextDelta  
<br />

textstring(optional)  
No description provided.
annotationsAnnotation(optional)  
Citation information for model-generated content.
Citation information for model-generated content.

#### Fields

start_indexinteger(optional)  
Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.  
end_indexinteger(optional)  
End of the attributed segment, exclusive.  
sourcestring(optional)  
Source attributed for a portion of the text. Could be a URL, title, or other identifier.  
typeobject(required)  
No description provided.

Always set to`"text"`.
ImageDelta  
<br />

datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeImageMimeTypeOption(optional)  
No description provided.

Possible values:

- `image/png`
- `image/jpeg`
- `image/webp`
- `image/heic`
- `image/heif`

The mime type of the image.
resolutionMediaResolution(optional)  
The resolution of the media.

Possible values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

typeobject(required)  
No description provided.

Always set to`"image"`.
AudioDelta  
<br />

datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeAudioMimeTypeOption(optional)  
No description provided.

Possible values:

- `audio/wav`
- `audio/mp3`
- `audio/aiff`
- `audio/aac`
- `audio/ogg`
- `audio/flac`

The mime type of the audio.  
typeobject(required)  
No description provided.

Always set to`"audio"`.
DocumentDelta  
<br />

datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeDocumentMimeTypeOption(optional)  
No description provided.

Possible values:

- `application/pdf`

The mime type of the document.  
typeobject(required)  
No description provided.

Always set to`"document"`.
VideoDelta  
<br />

datastring(optional)  
No description provided.  
uristring(optional)  
No description provided.
mime_typeVideoMimeTypeOption(optional)  
No description provided.

Possible values:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

The mime type of the video.
resolutionMediaResolution(optional)  
The resolution of the media.

Possible values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

typeobject(required)  
No description provided.

Always set to`"video"`.
ThoughtSummaryDelta  
<br />

typeobject(required)  
No description provided.

Always set to`"thought_summary"`.  
content[ImageContent](https://ai.google.dev/api/interactions-api#Resource:ImageContent)or[TextContent](https://ai.google.dev/api/interactions-api#Resource:TextContent)(optional)  
No description provided.
ThoughtSignatureDelta  
<br />

signaturestring(optional)  
Signature to match the backend source to be part of the generation.  
typeobject(required)  
No description provided.

Always set to`"thought_signature"`.
FunctionCallDelta  
<br />

namestring(optional)  
No description provided.  
argumentsobject(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"function_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
FunctionResultDelta  
<br />

namestring(optional)  
No description provided.  
is_errorboolean(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"function_result"`.  
resultobject or string(optional)  
Tool call result delta.  
call_idstring(optional)  
ID to match the ID from the function call block.
CodeExecutionCallDelta  
<br />

argumentsCodeExecutionCallArguments(optional)  
No description provided.
The arguments to pass to the code execution.

#### Fields

languageenum (string)(optional)  
Programming language of the \`code\`.

Possible values:

- `python`  
codestring(optional)  
The code to be executed.  
typeobject(required)  
No description provided.

Always set to`"code_execution_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
CodeExecutionResultDelta  
<br />

resultstring(optional)  
No description provided.  
is_errorboolean(optional)  
No description provided.  
signaturestring(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"code_execution_result"`.  
call_idstring(optional)  
ID to match the ID from the function call block.
UrlContextCallDelta  
<br />

argumentsUrlContextCallArguments(optional)  
No description provided.
The arguments to pass to the URL context.

#### Fields

urlsarray (string)(optional)  
The URLs to fetch.  
typeobject(required)  
No description provided.

Always set to`"url_context_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
UrlContextResultDelta  
<br />

signaturestring(optional)  
No description provided.
resultUrlContextResult(optional)  
No description provided.
The result of the URL context.

#### Fields

urlstring(optional)  
The URL that was fetched.  
statusenum (string)(optional)  
The status of the URL retrieval.

Possible values:

- `success`
- `error`
- `paywall`
- `unsafe`  
is_errorboolean(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"url_context_result"`.  
call_idstring(optional)  
ID to match the ID from the function call block.
GoogleSearchCallDelta  
<br />

argumentsGoogleSearchCallArguments(optional)  
No description provided.
The arguments to pass to Google Search.

#### Fields

queriesarray (string)(optional)  
Web search queries for the following-up web search.  
typeobject(required)  
No description provided.

Always set to`"google_search_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
GoogleSearchResultDelta  
<br />

signaturestring(optional)  
No description provided.
resultGoogleSearchResult(optional)  
No description provided.
The result of the Google Search.

#### Fields

urlstring(optional)  
URI reference of the search result.  
titlestring(optional)  
Title of the search result.  
rendered_contentstring(optional)  
Web content snippet that can be embedded in a web page or an app webview.  
is_errorboolean(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"google_search_result"`.  
call_idstring(optional)  
ID to match the ID from the function call block.
McpServerToolCallDelta  
<br />

namestring(optional)  
No description provided.  
server_namestring(optional)  
No description provided.  
argumentsobject(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"mcp_server_tool_call"`.  
idstring(optional)  
A unique ID for this specific tool call.
McpServerToolResultDelta  
<br />

namestring(optional)  
No description provided.  
server_namestring(optional)  
No description provided.  
typeobject(required)  
No description provided.

Always set to`"mcp_server_tool_result"`.  
resultobject or string(optional)  
Tool call result delta.  
call_idstring(optional)  
ID to match the ID from the function call block.
FileSearchResultDelta  
<br />

resultFileSearchResult(optional)  
No description provided.
The result of the File Search.

#### Fields

titlestring(optional)  
The title of the search result.  
textstring(optional)  
The text of the search result.  
file_search_storestring(optional)  
The name of the file search store.  
typeobject(required)  
No description provided.

Always set to`"file_search_result"`.
ContentStop  
<br />

indexinteger(optional)  
No description provided.  
event_typestring(optional)  
No description provided.

Always set to`"content.stop"`.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.
ErrorEvent  
<br />

event_typestring(optional)  
No description provided.

Always set to`"error"`.
errorError(optional)  
No description provided.
Error message from an interaction.

#### Fields

codestring(optional)  
A URI that identifies the error type.  
messagestring(optional)  
A human-readable error message.  
event_idstring(optional)  
The event_id token to be used to resume the interaction stream, from this event.  

### Examples

### Interaction Start

```json
{
  "event_type": "interaction.start",
  "interaction": {
    "id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
    "model": "gemini-2.5-flash",
    "object": "interaction",
    "status": "in_progress"
  }
}
```

### Interaction Complete

```json
{
  "event_type": "interaction.complete",
  "interaction": {
    "created": "2025-12-09T18:45:40Z",
    "id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
    "model": "gemini-2.5-flash",
    "object": "interaction",
    "outputs": [
      {
        "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0+19xcLsGG46bd8wjkF/6RNlRUdvHrXyjsHkG0BZFcuO/bPOyA6Xh5jANNgx82wPHjGExN8A4ZQn56FlMwyZoqFVQz0QyY1lfibFJ2zU3J87uw26OewzcuVX0KEcs+GIsZa3EA6WwqhbsOd3wtZB3Ua2Qf98VAWZTS5y/tWpql7jnU3/CU7pouxQr/Bwft3hwnJNesQ9/dDJTuaQ8Zprh9VRWf1aFFjpIueOjBRrlT3oW6/y/eRl/Gt9BQXCYTqg/38vHFUU4Wo/d9dUpvfCe/a3o97t2Jgxp34oFKcsVb4S5WJrykIkw+14DzVnTpCpbQNFckqvFLuqnJCkL0EQFtunBXI03FJpPu3T1XU6id8S7ojoJQZSauGUCgmaLqUGdMrd08oo81ecoJSLs51Re9N/lISGmjWFPGpqJLoGq6uo4FHz58hmeyXCgHG742BHz2P3MiH1CXHUT2J8mF6zLhf3SR9Qb3lkrobAh",
        "type": "thought"
      },
      {
        "text": "Elara\u2019s life was a symphony of quiet moments. A librarian, she found solace in the hushed aisles, the scent of aged paper, and the predictable rhythm of her days. Her small apartment, meticulously ordered, reflected this internal calm, save",
        "type": "text"
      },
      {
        "text": " for one beloved anomaly: a chipped porcelain teacup, inherited from her grandmother, which held her morning Earl Grey.\n\nOne Tuesday, stirring her tea, Elara paused. At the bottom, nestled against the porcelain, was a star.",
        "type": "text"
      },
      {
        "text": " Not a star-shaped tea leaf, but a miniature, perfectly formed celestial body, radiating a faint, cool luminescence. Before she could gasp, it dissolved, leaving only the amber swirl of her brew. She dismissed it as a trick of",
        "type": "text"
      },
      {
        "text": " tired eyes.\n\nBut the next morning, a gossamer-thin feather, smaller than an eyelash and shimmering with iridescent hues, floated on the surface. It vanished the moment she tried to touch it. A week later, a single,",
        "type": "text"
      },
      {
        "text": " impossibly delicate bloom, like spun moonbeam, unfolded in her cup before fading into nothingness.\n\nThese weren't illusions. Each day, Elara\u2019s chipped teacup offered a fleeting, exquisite secret. A tiny, perfect",
        "type": "text"
      },
      {
        "text": " crystal, a miniature spiral nebula, a fragment of rainbow caught in liquid form. They never lingered, never accumulated, simply *were* and then *weren't*, leaving behind a residue of quiet wonder.\n\nElara never spoke",
        "type": "text"
      },
      {
        "text": " of it. It was her private wellspring, a daily reminder that magic could exist in the smallest, most overlooked corners of the world. Her routine remained unchanged, her external life a picture of calm, but inside, a secret garden blo",
        "type": "text"
      },
      {
        "text": "omed. Each dawn brought not just tea, but the silent promise of extraordinary beauty, waiting patiently in a chipped teacup.",
        "type": "text"
      }
    ],
    "role": "model",
    "status": "completed",
    "updated": "2025-12-09T18:45:40Z",
    "usage": {
      "input_tokens_by_modality": [
        {
          "modality": "text",
          "tokens": 11
        }
      ],
      "total_cached_tokens": 0,
      "total_input_tokens": 11,
      "total_output_tokens": 364,
      "total_reasoning_tokens": 1120,
      "total_tokens": 1495,
      "total_tool_use_tokens": 0
    }
  }
}
```

### Interaction Status Update

```json
{
  "event_type": "interaction.status_update",
  "interaction_id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
  "status": "in_progress"
}
```

### Content Start

```json
{
  "event_type": "content.start",
  "content": {
    "type": "text"
  },
  "index": 1
}
```

### Content Delta

```json
{
  "event_type": "content.delta",
  "delta": {
    "type": "text",
    "text": "Elara\u2019s life was a symphony of quiet moments. A librarian, she found solace in the hushed aisles, the scent of aged paper, and the predictable rhythm of her days. Her small apartment, meticulously ordered, reflected this internal calm, save"
  },
  "index": 1
}
```

### Content Stop

```json
{
  "event_type": "content.stop",
  "index": 1
}
```

### Error Event

```json
{
  "event_type": "error",
  "error": {
    "message": "Failed to get completed interaction: Result not found.",
    "code": "not_found"
  }
}
```