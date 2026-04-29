import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { ChatPathCourse } from "../src/chat_models.js";

describe("ChatPathCourse", () => {
  const originalKey = process.env.PCH_API_KEY;

  beforeEach(() => {
    delete process.env.PCH_API_KEY;
  });

  afterEach(() => {
    if (originalKey !== undefined) process.env.PCH_API_KEY = originalKey;
  });

  it("throws without an API key", () => {
    expect(() => new ChatPathCourse()).toThrow(/PCH API key required/);
  });

  it("uses PCH_API_KEY env var when present", () => {
    process.env.PCH_API_KEY = "pch_prod_b_test";
    const llm = new ChatPathCourse();
    expect(llm._llmType()).toBe("pathcourse");
  });

  it("accepts an explicit pchApiKey", () => {
    const llm = new ChatPathCourse({ pchApiKey: "pch_prod_b_explicit", model: "pch-pro" });
    expect(llm._llmType()).toBe("pathcourse");
  });
});
