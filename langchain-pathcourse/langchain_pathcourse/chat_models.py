"""
ChatPathCourse — LangChain chat model for PathCourse Health.

Usage:
    from langchain_pathcourse import ChatPathCourse

    llm = ChatPathCourse(
        model="pch-fast",
        pch_api_key="pch_prod_b_...",   # or set PCH_API_KEY env var
    )

    response = llm.invoke("Explain x402 in one sentence.")
    print(response.content)
"""

import os
from typing import Dict, Optional

from langchain_openai import ChatOpenAI

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"

PCH_MODELS = {
    "pch-fast":          "Fast reasoning, classification, routing — $0.44/M tokens",
    "pch-coder":         "Code generation, debugging — $3.50/M tokens",
    "pch-embed":         "Text embeddings for semantic search/RAG — $0.015/M tokens",
    "pch-translate":     "Multilingual translation — $0.08/M chars",
    "pch-pro":           "Deep reasoning, multi-step planning — $1.96/M tokens (Bronze+)",
    "pch-audio":         "Text-to-speech, standard quality — $1.85/M chars (Bronze+)",
    "pch-documents":     "Document parsing/OCR — $0.26 in / $1.48 out per M tokens (Bronze+)",
    "pch-transcribe":    "Speech-to-text — $0.0008/minute (Bronze+)",
    "pch-extract":       "Structured data extraction — $0.012/M tokens (Bronze+)",
    "pch-rerank":        "Reranking for RAG pipelines — $0.025/M tokens (Bronze+)",
    "pch-image":         "Text-to-image — $0.028/image (Silver+)",
    "pch-audio-premium": "Text-to-speech, premium quality — $37.00/M chars (Silver+)",
    "pch-talk":          "Voice conversation — $0.001/minute (Silver+)",
    "claude-haiku":      "Anthropic Claude Haiku — common rate (Silver+)",
    "claude-sonnet":     "Anthropic Claude Sonnet — common rate (Gold)",
}


class ChatPathCourse(ChatOpenAI):
    """
    LangChain ChatModel for PathCourse Health.

    Drop-in replacement for ChatOpenAI. Uses the PCH gateway which is
    fully OpenAI API-compatible. Adds PCH-specific config and error handling.

    Args:
        model: PCH model name. Default "pch-fast".
               Options: pch-fast, pch-pro, pch-coder, claude-haiku, claude-sonnet
        pch_api_key: Your PCH API key (pch_prod_b_...). Falls back to PCH_API_KEY env var.

    Example:
        llm = ChatPathCourse(model="pch-pro")
        chain = prompt | llm | StrOutputParser()
        result = chain.invoke({"topic": "x402 protocol"})
    """

    def __init__(self, model: str = "pch-fast", pch_api_key: Optional[str] = None, **kwargs):
        api_key = pch_api_key or os.environ.get("PCH_API_KEY")
        if not api_key:
            raise ValueError(
                "PCH API key required. Pass pch_api_key= or set the PCH_API_KEY environment variable. "
                "Get a key at https://pathcoursehealth.com"
            )

        super().__init__(
            model=model,
            api_key=api_key,
            base_url=PCH_GATEWAY,
            **kwargs,
        )

    @property
    def _llm_type(self) -> str:
        return "pathcourse"

    @classmethod
    def list_models(cls) -> Dict[str, str]:
        """Return all available PCH models with descriptions."""
        return PCH_MODELS
