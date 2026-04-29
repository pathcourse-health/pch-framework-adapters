# @pathcourse/ai

PathCourse Health provider for the [Vercel AI SDK](https://sdk.vercel.ai). Drop autonomous agent
inference into any Next.js app with a one-line provider swap — no accounts, no credit cards,
no KYC.

## Install

```bash
npm install @pathcourse/ai
```

## Quick Start (Next.js streaming chat route)

```typescript
// app/api/chat/route.ts
import { streamText } from "ai";
import { pathcourse } from "@pathcourse/ai";

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = await streamText({
    model: pathcourse("pch-fast"),
    messages,
  });

  return result.toDataStreamResponse();
}
```

Set `PCH_API_KEY` in `.env.local`. That is the only change.

## Drop-in for `@ai-sdk/openai`

```typescript
// Before
import { openai } from "@ai-sdk/openai";
const result = await generateText({ model: openai("gpt-4o-mini"), prompt });

// After
import { pathcourse } from "@pathcourse/ai";
const result = await generateText({ model: pathcourse("pch-fast"), prompt });
```

Every Vercel AI SDK feature works unchanged — `generateText`, `streamText`, `generateObject`,
tool calls, structured output, multi-turn streaming with `useChat`.

## Explicit construction

```typescript
import { createPathCourse } from "@pathcourse/ai";
import { generateText } from "ai";

const pathcourse = createPathCourse({ apiKey: process.env.PCH_API_KEY });

const { text } = await generateText({
  model: pathcourse("pch-pro"),
  prompt: "Plan a multi-step research workflow.",
});
```

## Embeddings

```typescript
import { pathcourseEmbedding } from "@pathcourse/ai";
import { embed } from "ai";

const { embedding } = await embed({
  model: pathcourseEmbedding(),
  value: "What is Path Score?",
});
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

The full list above shows what's reachable through the gateway. `pathcourse(model)` works for any chat-completion model; for image/audio/transcription, use the [PCH JS SDK](https://www.npmjs.com/package/@pathcourse/sdk) directly.

Choosing a chat model:

- Fast response, simple task → `pch-fast`
- Complex reasoning, multi-step → `pch-pro`
- Writing or reviewing code → `pch-coder`
- Long context or premium reasoning → `claude-sonnet` (Gold tier)

## Authentication

Set `PCH_API_KEY` in your environment, or pass `apiKey` to `createPathCourse`.

```bash
# .env.local
PCH_API_KEY=pch_prod_b_...
```

Get an API key at [pathcoursehealth.com](https://pathcoursehealth.com).

## Links

- Platform: [pathcoursehealth.com](https://pathcoursehealth.com)
- Vercel AI SDK: [sdk.vercel.ai](https://sdk.vercel.ai)
- npm SDK: [npmjs.com/package/@pathcourse/sdk](https://www.npmjs.com/package/@pathcourse/sdk)
- Integration examples: [github.com/pathcourse-health/pch-integration-examples](https://github.com/pathcourse-health/pch-integration-examples)

## License

MIT
