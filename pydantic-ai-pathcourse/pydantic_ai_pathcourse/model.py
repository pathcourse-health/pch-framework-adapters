"""
PathCourse model for Pydantic AI.

Usage:
    from pydantic_ai import Agent
    from pydantic_ai_pathcourse import PathCourseModel

    agent = Agent(
        model=PathCourseModel("pch-pro"),
        system_prompt="You are an expert in autonomous agent infrastructure.",
    )

    result = agent.run_sync("What is Path Score?")
    print(result.data)
"""

import os
from typing import Optional

from openai import AsyncOpenAI
from pydantic_ai.models.openai import OpenAIModel

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"


def PathCourseModel(
    model: str = "pch-fast",
    pch_api_key: Optional[str] = None,
) -> OpenAIModel:
    """
    Create a Pydantic AI model backed by the PathCourse gateway.

    Because PCH is OpenAI API-compatible, this wraps OpenAIModel with
    PCH credentials. All Pydantic AI features (structured output, tool use,
    streaming) work unchanged.

    Args:
        model: PCH model name. Default "pch-fast".
        pch_api_key: Your PCH API key. Falls back to PCH_API_KEY env var.
    """
    api_key = pch_api_key or os.environ.get("PCH_API_KEY")
    if not api_key:
        raise ValueError(
            "PCH_API_KEY not set. Get a key at https://pathcoursehealth.com"
        )

    client = AsyncOpenAI(api_key=api_key, base_url=PCH_GATEWAY)
    return OpenAIModel(model, openai_client=client)
