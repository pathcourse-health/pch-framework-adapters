"""Tests for PathCourseEmbeddings — run with: pytest tests/"""

import os
from unittest.mock import patch

import pytest

from langchain_pathcourse import PathCourseEmbeddings


def test_raises_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        os.environ.pop("PCH_API_KEY", None)
        with pytest.raises(ValueError, match="PCH_API_KEY not set"):
            PathCourseEmbeddings()


def test_initialises_with_env_var():
    with patch.dict(os.environ, {"PCH_API_KEY": "pch_prod_b_test"}):
        emb = PathCourseEmbeddings()
        assert emb.api_key == "pch_prod_b_test"


def test_initialises_with_explicit_key():
    emb = PathCourseEmbeddings(pch_api_key="pch_prod_b_explicit")
    assert emb.api_key == "pch_prod_b_explicit"
