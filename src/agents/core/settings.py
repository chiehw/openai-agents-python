"""
Settings module for OpenAI Agents.

This module provides a centralized configuration management system using pydantic-settings.
It automatically reads configuration from environment variables and .env files.
"""

from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Global settings for OpenAI Agents.

    This class automatically loads configuration from environment variables and .env files.
    The priority order is:
    1. Environment variables
    2. .env file values
    3. Default values specified in this class
    """

    # OpenAI API configuration
    OPENAI_API_KEY: Optional[str] = Field(
        description="OpenAI API 密钥",
        default=None,
    )
    OPENAI_BASE_URL: Optional[str] = Field(
        description="OpenAI API 基础 URL",
        default=None,
    )

    # HTTP proxy configuration
    HTTP_PROXY: Optional[str] = Field(
        description="HTTP 代理服务器地址",
        default=None,
    )
    HTTPS_PROXY: Optional[str] = Field(
        description="HTTPS 代理服务器地址",
        default=None,
    )

    ENABLE_RESPONSE_API: bool = Field(
        description="是否启用 Responses API",
        default=True,
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


# Global settings instance
settings = Settings()
