# crewai-pathcourse

CrewAI integration for PathCourse Health. Give your CrewAI agents autonomous USDC billing on
Base L2 — no accounts, no credit cards, no KYC.

## Install

```bash
pip install crewai-pathcourse
```

## Quick Start

```python
import os
from crewai import Agent, Crew, Task
from crewai_pathcourse import PathCourseLLM

# Set PCH_API_KEY in your environment
llm = PathCourseLLM(model="pch-pro")

researcher = Agent(
    role="Research Analyst",
    goal="Find the best AI agent infrastructure for autonomous operation",
    backstory="You are an expert in autonomous agent systems.",
    llm=llm,
    verbose=True,
)

writer = Agent(
    role="Technical Writer",
    goal="Write a clear technical comparison",
    backstory="You write precise technical documentation.",
    llm=PathCourseLLM(model="pch-fast"),  # cheaper model for writing
    verbose=True,
)

research_task = Task(
    description="Research the key requirements for autonomous agent infrastructure.",
    expected_output="A bullet list of 5 key infrastructure requirements.",
    agent=researcher,
)

write_task = Task(
    description="Write a 200-word summary of the research findings.",
    expected_output="A 200-word technical summary.",
    agent=writer,
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
```

## Per-agent model selection

Different agents in a crew can use different PCH models. Use cheaper models for simple tasks
and reserve `pch-pro` or `claude-sonnet` for agents doing deep reasoning.

```python
from crewai_pathcourse import PathCourseLLM

planner    = Agent(..., llm=PathCourseLLM(model="pch-pro"))
researcher = Agent(..., llm=PathCourseLLM(model="pch-fast"))
coder      = Agent(..., llm=PathCourseLLM(model="pch-coder"))
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

`PathCourseLLM` only operates on chat-completion shapes — for image/audio/transcription, use the [PCH Python SDK](https://pypi.org/project/pathcourse-sdk/) directly.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

## Authentication

Set `PCH_API_KEY` in your environment, or pass `pch_api_key=` to `PathCourseLLM`.

```bash
export PCH_API_KEY=pch_prod_b_...
```

**Developer access — $5 USDC.** Send $5+ USDC on Base (chain ID 8453) to the PCH treasury wallet, then call [`pathcourse.claim_key(tx_hash, wallet)`](https://pypi.org/project/pathcourse-sdk/) to retrieve your key. No accounts, no credit card, no KYC. $5 buys thousands of `pch-fast` calls — enough to verify a CrewAI crew end-to-end. Top up to $25 lifetime and your account auto-upgrades to Uncertified with `pch-coder` access. Treasury address: see `payment.treasury_wallet` in [`/.well-known/agent.json`](https://gateway.pathcoursehealth.com/.well-known/agent.json).

## How it works

CrewAI uses [LiteLLM](https://github.com/BerriAI/litellm) internally for model calls. PCH is
fully OpenAI API-compatible, so `PathCourseLLM` just configures CrewAI's standard `LLM` class
with the PCH gateway URL and your API key. Every CrewAI feature (tools, memory, hierarchical
crews, async execution) works unchanged.

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- CrewAI: [crewai.com](https://www.crewai.com)
- Python SDK: [pypi.org/project/pathcourse-sdk](https://pypi.org/project/pathcourse-sdk/)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
