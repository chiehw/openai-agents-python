from __future__ import annotations

from openai import AsyncOpenAI

_default_openai_key: str | None = None
_default_openai_client: AsyncOpenAI | None = None
_use_responses_by_default: bool = True

def set_default_openai_key(key: str) -> None:
    global _default_openai_key
    _default_openai_key = key


def get_default_openai_key() -> str | None:
    # return _default_openai_key
    # CHIEH-start
    # 优先使用settings，若不存在则尝试从内部缓存获取
    try:
        from agents.core.settings import settings
        return settings.OPENAI_API_KEY
    except (ImportError, AttributeError):
        from agents.logger import logger
        logger.warning("Failed to import settings from core.settings, use default value")
        return _default_openai_key
    # CHIEH-end


def set_default_openai_client(client: AsyncOpenAI) -> None:
    global _default_openai_client
    _default_openai_client = client


def get_default_openai_client() -> AsyncOpenAI | None:
    return _default_openai_client


def set_use_responses_by_default(use_responses: bool) -> None:
    global _use_responses_by_default
    _use_responses_by_default = use_responses


def get_use_responses_by_default() -> bool:
    # return _use_responses_by_default
    # CHIEH-start
    # 优先使用settings，若不存在则尝试从内部缓存获取
    try:
        from agents.core.settings import settings
        return settings.ENABLE_RESPONSE_API
    except (ImportError, AttributeError):
        from agents.logger import logger
        logger.warning("Failed to import settings from core.settings, use default value")
        return _use_responses_by_default
    # CHIEH-end
