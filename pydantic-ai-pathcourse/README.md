# pydantic-ai-pathcourse

[Pydantic AI](https://ai.pydantic.dev) integration for PathCourse Health. Build typed,
production-grade agents with autonomous USDC billing on Base L2 — no accounts, no credit
cards, no KYC.

## Install

```bash
pip install pydantic-ai-pathcourse
```

## Quick Start

```python
from pydantic_ai import Agent
from pydantic_ai_pathcourse import PathCourseModel

agent = Agent(
    model=PathCourseModel("pch-pro"),
    system_prompt="You are an expert in autonomous agent infrastructure.",
)

result = agent.run_sync("What is Path Score?")
print(result.data)
```

## Structured output

Pydantic AI's structured-output guarantees work unchanged with PCH:

```python
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai_pathcourse import PathCourseModel


class InfraReport(BaseModel):
    summary: str
    requirements: list[str]
    risk_level: int


agent = Agent(
    model=PathCourseModel("pch-pro"),
    result_type=InfraReport,
)

result = agent.run_sync("Analyze autonomous agent infrastructure for a fintech startup.")
print(result.data.requirements)
```

## Tool use

```python
from pydantic_ai import Agent, RunContext
from pydantic_ai_pathcourse import PathCourseModel

agent = Agent(model=PathCourseModel("pch-pro"))

@agent.tool
async def get_balance(ctx: RunContext[None], agent_id: str) -> float:
    """Look up the USDC balance for a PCH agent."""
    return 42.50

result = agent.run_sync("What is the balance for agent abc123?")
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

`PathCourseModel` only operates on chat-completion shapes — for image/audio/transcription, use the [PCH Python SDK](https://pypi.org/project/pathcourse-sdk/) directly.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

## Authentication

Set `PCH_API_KEY` in your environment, or pass `pch_api_key=` to `PathCourseModel`.

```bash
export PCH_API_KEY=pch_prod_b_...
```

**Developer access — $5 USDC.** Send $5+ USDC on Base (chain ID 8453) to the PCH treasury wallet, then call [`pathcourse.claim_key(tx_hash, wallet)`](https://pypi.org/project/pathcourse-sdk/) to retrieve your key. No accounts, no credit card, no KYC. $5 buys thousands of `pch-fast` calls — enough to verify any typed-agent integration. Top up to $25 lifetime and your account auto-upgrades to Uncertified with `pch-coder` access. Treasury address: see `payment.treasury_wallet` in [`/.well-known/agent.json`](https://gateway.pathcoursehealth.com/.well-known/agent.json).

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- Pydantic AI: [ai.pydantic.dev](https://ai.pydantic.dev)
- Python SDK: [pypi.org/project/pathcourse-sdk](https://pypi.org/project/pathcourse-sdk/)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
