"""Tests for PathCourseLLM — run with: pytest tests/"""

import os
from unittest.mock import patch

import pytest

from crewai_pathcourse import PathCourseLLM


def test_raises_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        os.environ.pop("PCH_API_KEY", None)
        with pytest.raises(ValueError, match="PCH API key required"):
            PathCourseLLM()


def test_initialises_with_env_var():
    with patch.dict(os.environ, {"PCH_API_KEY": "pch_prod_b_test"}):
        llm = PathCourseLLM()
        assert "pch-fast" in llm.model
        assert llm.base_url == "https://gateway.pathcoursehealth.com/v1"


def test_initialises_with_explicit_key_and_model():
    llm = PathCourseLLM(pch_api_key="pch_prod_b_test", model="pch-pro")
    assert "pch-pro" in llm.model
