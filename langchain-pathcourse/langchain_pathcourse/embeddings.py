"""
PathCourseEmbeddings — LangChain embeddings for PathCourse Health.

Usage:
    from langchain_pathcourse import PathCourseEmbeddings

    embeddings = PathCourseEmbeddings()
    vector = embeddings.embed_query("What is Path Score?")
    vectors = embeddings.embed_documents(["doc1", "doc2"])
"""

import os
from typing import List, Optional

import httpx
from langchain_core.embeddings import Embeddings

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"


class PathCourseEmbeddings(Embeddings):
    """
    LangChain Embeddings backed by the PCH pch-embed model.
    Fully compatible with LangChain vector stores (FAISS, Chroma, Pinecone, etc.)

    Args:
        pch_api_key: Your PCH API key. Falls back to PCH_API_KEY env var.
    """

    def __init__(self, pch_api_key: Optional[str] = None):
        self.api_key = pch_api_key or os.environ.get("PCH_API_KEY")
        if not self.api_key:
            raise ValueError("PCH_API_KEY not set. Get a key at https://pathcoursehealth.com")

    def _embed(self, texts: List[str]) -> List[List[float]]:
        resp = httpx.post(
            f"{PCH_GATEWAY}/embeddings",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"model": "pch-embed", "input": texts},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return [item["embedding"] for item in sorted(data["data"], key=lambda x: x["index"])]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts)

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]
