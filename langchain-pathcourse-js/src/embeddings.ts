import { OpenAIEmbeddings } from "@langchain/openai";

const PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1";

/**
 * PathCourseEmbeddings — LangChain.js Embeddings backed by pch-embed.
 * Compatible with all LangChain vector stores (FAISS, Chroma, Pinecone, etc.)
 */
export class PathCourseEmbeddings extends OpenAIEmbeddings {
  constructor(pchApiKey?: string) {
    const apiKey = pchApiKey ?? process.env.PCH_API_KEY;
    if (!apiKey) {
      throw new Error(
        "PCH_API_KEY not set. Get a key at https://pathcoursehealth.com",
      );
    }
    super({
      model: "pch-embed",
      apiKey,
      configuration: { baseURL: PCH_GATEWAY },
    });
  }
}
