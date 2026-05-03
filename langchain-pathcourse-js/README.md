# @pathcourse/langchain

LangChain.js integration for PathCourse Health. Autonomous agent inference with USDC billing
on Base L2 — no accounts, no credit cards, no KYC.

## Install

```bash
npm install @pathcourse/langchain
```

## Quick Start

```typescript
import { ChatPathCourse } from "@pathcourse/langchain";
import { ChatPromptTemplate } from "@langchain/core/prompts";

const llm = new ChatPathCourse({ model: "pch-fast" });   // set PCH_API_KEY env var

const prompt = ChatPromptTemplate.fromTemplate("Explain {topic} in one paragraph.");
const chain = prompt.pipe(llm);
const result = await chain.invoke({ topic: "autonomous agent billing" });
console.log(result.content);
```

## Drop-in replacement for ChatOpenAI

```typescript
// Before
import { ChatOpenAI } from "@langchain/openai";
const llm = new ChatOpenAI({ model: "gpt-4o-mini" });

// After
import { ChatPathCourse } from "@pathcourse/langchain";
const llm = new ChatPathCourse({ model: "pch-fast" });
```

Every LangChain chain, agent, tool, and memory module keeps working unchanged.

## Embeddings

```typescript
import { PathCourseEmbeddings } from "@pathcourse/langchain";
import { MemoryVectorStore } from "langchain/vectorstores/memory";

const embeddings = new PathCourseEmbeddings();
const store = await MemoryVectorStore.fromTexts(
  ["hello world", "goodbye world"],
  [{}, {}],
  embeddings,
);
const results = await store.similaritySearch("greeting");
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

The full list above shows what's reachable through the gateway. `ChatPathCourse` and `PathCourseEmbeddings` only operate on chat-completion and embedding shapes — for image, audio, transcription, etc., use the [PCH JS SDK](https://www.npmjs.com/package/@pathcourse/sdk) directly.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

## Authentication

Set `PCH_API_KEY` in your environment, or pass `pchApiKey` to the constructor.

```bash
export PCH_API_KEY=pch_prod_b_...
```

**Developer access — $5 USDC.** Send $5+ USDC on Base (chain ID 8453) to the PCH treasury wallet, then call [`claimKey({ txHash, wallet })`](https://www.npmjs.com/package/@pathcourse/sdk) to retrieve your key. No accounts, no credit card, no KYC. $5 buys thousands of `pch-fast` calls — enough to verify any integration. Top up to $25 lifetime and your account auto-upgrades to Uncertified with `pch-coder` access. Treasury address: see `payment.treasury_wallet` in [`/.well-known/agent.json`](https://gateway.pathcoursehealth.com/.well-known/agent.json).

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- npm SDK: [npmjs.com/package/@pathcourse/sdk](https://www.npmjs.com/package/@pathcourse/sdk)
- Python SDK: [pypi.org/project/pathcourse-sdk](https://pypi.org/project/pathcourse-sdk/)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
