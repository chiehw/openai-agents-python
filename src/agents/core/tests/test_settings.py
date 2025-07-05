"""Tests for settings module."""

import os
from unittest import mock

import pytest

from core.settings import Settings


def test_settings_from_env():
    """Test that settings can be loaded from environment variables."""
    with mock.patch.dict(os.environ, {
        "OPENAI_API_KEY": "test-api-key",
        "OPENAI_BASE_URL": "https://test-api.openai.com",
        "HTTP_PROXY": "http://test-proxy:8080",
    }):
        settings = Settings()
        assert settings.OPENAI_API_KEY == "test-api-key"
        assert settings.OPENAI_BASE_URL == "https://test-api.openai.com"
        assert settings.HTTP_PROXY == "http://test-proxy:8080"


def test_settings_defaults():
    """Test that settings have correct defaults when not set."""
    with mock.patch.dict(os.environ, {}, clear=True):
        settings = Settings()
        assert settings.OPENAI_API_KEY is None
        assert settings.OPENAI_BASE_URL is None
        assert settings.HTTP_PROXY is None 