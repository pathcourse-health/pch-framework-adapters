"""
PathCourseLLM — CrewAI LLM for PathCourse Health.

Usage:
    from crewai import Agent, Crew, Task
    from crewai_pathcourse import PathCourseLLM

    llm = PathCourseLLM(model="pch-pro")

    researcher = Agent(
        role="Research Analyst",
        goal="Analyze autonomous agent infrastructure trends",
        backstory="Expert in AI agent systems and web3 infrastructure",
        llm=llm,
    )
"""

import os
from typing import Optional

from crewai import LLM

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"


def PathCourseLLM(
    model: str = "pch-fast",
    pch_api_key: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> LLM:
    """
    Create a CrewAI LLM configured for the PathCourse Health gateway.

    Returns a standard CrewAI LLM instance. Pass it to any Agent's llm= parameter.

    Args:
        model: PCH model name. Default "pch-fast".
               Tip: Use "pch-pro" for agents doing deep reasoning or planning.
               Use "pch-coder" for agents that write or review code.
        pch_api_key: Your PCH API key. Falls back to PCH_API_KEY env var.
        temperature: Sampling temperature. Default 0.7.
        max_tokens: Max tokens to generate. Default 4096.
    """
    api_key = pch_api_key or os.environ.get("PCH_API_KEY")
    if not api_key:
        raise ValueError(
            "PCH API key required. Pass pch_api_key= or set PCH_API_KEY env var.\n"
            "Get a key at https://pathcoursehealth.com"
        )

    return LLM(
        model=f"openai/{model}",
        api_key=api_key,
        base_url=PCH_GATEWAY,
        temperature=temperature,
        max_tokens=max_tokens,
    )
