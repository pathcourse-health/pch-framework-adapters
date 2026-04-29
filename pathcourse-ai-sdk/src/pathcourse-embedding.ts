import { createPathCourse } from "./pathcourse-provider.js";

/**
 * Convenience helper for the PCH embedding model.
 *
 * @example
 * import { pathcourseEmbedding } from "@pathcourse/ai";
 * import { embed } from "ai";
 *
 * const { embedding } = await embed({
 *   model: pathcourseEmbedding(),
 *   value: "What is Path Score?",
 * });
 */
export function pathcourseEmbedding(options: { apiKey?: string } = {}) {
  const provider = createPathCourse(options);
  return provider.embedding("pch-embed");
}
