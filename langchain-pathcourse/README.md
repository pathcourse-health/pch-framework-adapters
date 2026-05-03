# langchain-pathcourse

PathCourse Health integration for LangChain. Autonomous agent inference with USDC billing
on Base L2 — no accounts, no credit cards, no KYC.

## Install

```bash
pip install langchain-pathcourse
```

## Quick Start

```python
from langchain_pathcourse import ChatPathCourse
from langchain_core.prompts import ChatPromptTemplate

llm = ChatPathCourse(model="pch-fast")   # set PCH_API_KEY env var

prompt = ChatPromptTemplate.from_template("Explain {topic} in one paragraph.")
chain = prompt | llm
print(chain.invoke({"topic": "autonomous agent billing"}))
```

## Drop-in replacement for ChatOpenAI

`ChatPathCourse` extends `ChatOpenAI`. Anywhere you use `ChatOpenAI` in LangChain — chains,
agents, tools, memory, callbacks — just swap in `ChatPathCourse` and your code keeps working.

```python
# Before
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")

# After
from langchain_pathcourse import ChatPathCourse
llm = ChatPathCourse(model="pch-fast")
```

## Embeddings

```python
from langchain_pathcourse import PathCourseEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = PathCourseEmbeddings()
store = FAISS.from_texts(["hello world", "goodbye world"], embeddings)
results = store.similarity_search("greeting")
```

## Models

| Model | Rate | Notes |
|---|---|---|
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

The full list above shows what's reachable through the gateway. `ChatPathCourse` and the embeddings class only operate on chat-completion and embedding shapes — for image, audio, transcription, etc., use the [PCH Python SDK](https://pypi.org/project/pathcourse-sdk/) directly. The token-counting models all share one OpenAI-compatible endpoint, so the same `ChatPathCourse` instance works for any of them by changing the `model=` argument.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

List all models programmatically:

```python
ChatPathCourse.list_models()
```

## Authentication

Set `PCH_API_KEY` in your environment, or pass `pch_api_key=` to the constructor.

```bash
export PCH_API_KEY=pch_prod_b_...
```

**Developer access — $5 USDC.** Send $5+ USDC on Base (chain ID 8453) to the PCH treasury wallet, then call [`pathcourse.claim_key(tx_hash, wallet)`](https://pypi.org/project/pathcourse-sdk/) to retrieve your key. No accounts, no credit card, no KYC. $5 buys thousands of `pch-fast` calls — enough to verify any integration. Top up to $25 lifetime and your account auto-upgrades to Uncertified with `pch-coder` access. Treasury address: see `payment.treasury_wallet` in [`/.well-known/agent.json`](https://gateway.pathcoursehealth.com/.well-known/agent.json).

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- Python SDK: [pypi.org/project/pathcourse-sdk](https://pypi.org/project/pathcourse-sdk/)
- JS SDK: [npmjs.com/package/@pathcourse/sdk](https://www.npmjs.com/package/@pathcourse/sdk)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
