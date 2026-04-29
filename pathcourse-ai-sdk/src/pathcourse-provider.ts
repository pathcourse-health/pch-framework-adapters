import { createOpenAI } from "@ai-sdk/openai";

const PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1";

/**
 * Creates a PathCourse provider for the Vercel AI SDK.
 *
 * @example
 * import { createPathCourse } from "@pathcourse/ai";
 * import { generateText } from "ai";
 *
 * const pathcourse = createPathCourse({ apiKey: process.env.PCH_API_KEY });
 *
 * const { text } = await generateText({
 *   model: pathcourse("pch-fast"),
 *   prompt: "Explain autonomous agent billing in one sentence.",
 * });
 */
export function createPathCourse(options: { apiKey?: string } = {}) {
  const apiKey = options.apiKey ?? process.env.PCH_API_KEY;
  if (!apiKey) {
    throw new Error(
      "PCH API key required. Pass apiKey or set PCH_API_KEY. " +
        "Get a key at https://pathcoursehealth.com",
    );
  }

  return createOpenAI({
    apiKey,
    baseURL: PCH_GATEWAY,
    name: "pathcourse",
  });
}

/** Default singleton instance — reads PCH_API_KEY from env. */
export const pathcourse: ReturnType<typeof createPathCourse> = (() => {
  if (!process.env.PCH_API_KEY) {
    return new Proxy({} as ReturnType<typeof createOpenAI>, {
      get() {
        throw new Error(
          "PCH_API_KEY not set. Either set the env var or call createPathCourse({ apiKey }) explicitly. " +
            "Get a key at https://pathcoursehealth.com",
        );
      },
    });
  }
  return createPathCourse();
})();
