"""
PathCourse configuration builder for AutoGen / AG2.

Usage:
    from autogen_pathcourse import pch_config
    from autogen import AssistantAgent, UserProxyAgent

    config_list = pch_config(model="pch-pro")

    assistant = AssistantAgent(
        name="assistant",
        llm_config={"config_list": config_list},
    )
"""

import os
from typing import List, Optional

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"


def pch_config(
    model: str = "pch-fast",
    pch_api_key: Optional[str] = None,
) -> List[dict]:
    """
    Build an AutoGen config_list for the PathCourse gateway.

    Returns a list with a single config dict. Pass it to AssistantAgent
    or ConversableAgent via llm_config={"config_list": config_list}.

    Args:
        model: PCH model name. Default "pch-fast".
        pch_api_key: Your PCH API key. Falls back to PCH_API_KEY env var.
    """
    api_key = pch_api_key or os.environ.get("PCH_API_KEY")
    if not api_key:
        raise ValueError(
            "PCH_API_KEY not set. Get a key at https://pathcoursehealth.com"
        )

    return [
        {
            "model": model,
            "api_key": api_key,
            "base_url": PCH_GATEWAY,
            "api_type": "openai",
        }
    ]
