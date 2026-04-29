"""Tests for ChatPathCourse — run with: pytest tests/"""

import os
from unittest.mock import patch

import pytest

from langchain_pathcourse import ChatPathCourse


def test_raises_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        os.environ.pop("PCH_API_KEY", None)
        with pytest.raises(ValueError, match="PCH API key required"):
            ChatPathCourse()


def test_initialises_with_env_var():
    with patch.dict(os.environ, {"PCH_API_KEY": "pch_prod_b_test"}):
        llm = ChatPathCourse()
        assert llm.openai_api_base == "https://gateway.pathcoursehealth.com/v1"
        assert llm.model_name == "pch-fast"


def test_initialises_with_explicit_key():
    llm = ChatPathCourse(pch_api_key="pch_prod_b_test", model="pch-pro")
    assert llm.model_name == "pch-pro"


def test_list_models():
    models = ChatPathCourse.list_models()
    assert "pch-fast" in models
    assert "pch-pro" in models
    assert "pch-coder" in models


def test_llm_type():
    llm = ChatPathCourse(pch_api_key="pch_prod_b_test")
    assert llm._llm_type == "pathcourse"
