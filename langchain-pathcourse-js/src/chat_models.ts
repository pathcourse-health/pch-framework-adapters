import { ChatOpenAI, type ClientOptions } from "@langchain/openai";

const PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1";

export type PCHModel =
  | "pch-fast"
  | "pch-coder"
  | "pch-embed"
  | "pch-translate"
  | "pch-pro"
  | "pch-audio"
  | "pch-documents"
  | "pch-transcribe"
  | "pch-extract"
  | "pch-rerank"
  | "pch-image"
  | "pch-audio-premium"
  | "pch-talk"
  | "claude-haiku"
  | "claude-sonnet";

interface ChatPathCourseInput {
  model?: PCHModel;
  pchApiKey?: string;
  temperature?: number;
  maxTokens?: number;
  streaming?: boolean;
}

/**
 * ChatPathCourse — LangChain.js ChatModel for PathCourse Health.
 *
 * Drop-in replacement for ChatOpenAI. Works with all LangChain chains,
 * agents, and tools unchanged.
 *
 * @example
 * const llm = new ChatPathCourse({ model: "pch-fast" });
 * const result = await llm.invoke("Explain x402 in one sentence.");
 * console.log(result.content);
 */
export class ChatPathCourse extends ChatOpenAI {
  constructor({
    model = "pch-fast",
    pchApiKey,
    ...rest
  }: ChatPathCourseInput = {}) {
    const apiKey = pchApiKey ?? process.env.PCH_API_KEY;
    if (!apiKey) {
      throw new Error(
        "PCH API key required. Pass pchApiKey or set PCH_API_KEY env var. " +
          "Get a key at https://pathcoursehealth.com",
      );
    }

    super({
      model,
      apiKey,
      configuration: {
        baseURL: PCH_GATEWAY,
      } as ClientOptions,
      ...rest,
    });
  }

  _llmType(): string {
    return "pathcourse";
  }
}
