# autogen-pathcourse

AutoGen / [AG2](https://ag2.ai) integration for PathCourse Health. Run multi-agent
conversations with autonomous USDC billing on Base L2 — no accounts, no credit cards,
no KYC.

## Install

```bash
# AutoGen (legacy package name)
pip install autogen-pathcourse pyautogen

# AG2 (the new fork)
pip install autogen-pathcourse ag2
```

## Quick Start

```python
from autogen import AssistantAgent, UserProxyAgent
from autogen_pathcourse import pch_config

config_list = pch_config(model="pch-pro")
llm_config = {"config_list": config_list, "temperature": 0.7}

assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a helpful AI assistant.",
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    code_execution_config=False,
)

user_proxy.initiate_chat(assistant, message="Explain x402 in two sentences.")
```

## Mixed-model multi-agent setup

Use different PCH models for different agents in the same conversation:

```python
from autogen import AssistantAgent
from autogen_pathcourse import pch_config

planner = AssistantAgent(
    name="planner",
    llm_config={"config_list": pch_config(model="pch-pro")},
    system_message="You plan multi-step research.",
)

coder = AssistantAgent(
    name="coder",
    llm_config={"config_list": pch_config(model="pch-coder")},
    system_message="You implement what the planner specifies.",
)

reviewer = AssistantAgent(
    name="reviewer",
    llm_config={"config_list": pch_config(model="pch-fast")},
    system_message="You spot-check work for issues.",
)
```

## Models

| Model | Rate | Min tier | Notes |
|---|---|---|---|
| `pch-fast` | $0.44 / M tokens | uncertified | Fast reasoning, classification, routing |
| `pch-coder` | $3.50 / M tokens | uncertified | Code generation, debugging |
| `pch-embed` | $0.015 / M tokens | uncertified | Text embeddings for semantic search / RAG |
| `pch-translate` | $0.08 / M chars | uncertified | Multilingual translation |
| `pch-pro` | $1.96 / M tokens | bronze | Deep reasoning, multi-step planning |
| `pch-audio` | $1.85 / M chars | bronze | Text-to-speech, standard quality |
| `pch-documents` | $0.26 in / $1.48 out per M tokens | bronze | Document parsing / OCR |
| `pch-transcribe` | $0.0008 / minute | bronze | Speech-to-text |
| `pch-extract` | $0.012 / M tokens | bronze | Structured data extraction |
| `pch-rerank` | $0.025 / M tokens | bronze | Reranking for RAG pipelines |
| `pch-image` | $0.028 / image | silver | Text-to-image |
| `pch-audio-premium` | $37.00 / M chars | silver | Text-to-speech, premium quality |
| `pch-talk` | $0.001 / minute | silver | Voice conversation |
| `claude-haiku` | Common rate | silver | Anthropic Claude Haiku |
| `claude-sonnet` | Common rate | gold | Anthropic Claude Sonnet |

`pch_config` only operates on chat-completion shapes — for image/audio/transcription, use the [PCH Python SDK](https://pypi.org/project/pathcourse-sdk/) directly.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

## Authentication

Set `PCH_API_KEY` in your environment, or pass `pch_api_key=` to `pch_config`.

```bash
export PCH_API_KEY=pch_prod_b_...
```

Get an API key at [pathcoursehealth.com](https://pathcoursehealth.com).

## How it works

AutoGen's `config_list` accepts any OpenAI-compatible endpoint via the `base_url` and
`api_type: "openai"` fields. The PCH gateway is fully OpenAI API-compatible, so this adapter
is purely configuration — every AutoGen feature (group chat, code execution, function
calling, custom agents) works unchanged.

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- AutoGen: [microsoft.github.io/autogen](https://microsoft.github.io/autogen)
- AG2: [ag2.ai](https://ag2.ai)
- Python SDK: [pypi.org/project/pathcourse-sdk](https://pypi.org/project/pathcourse-sdk/)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
