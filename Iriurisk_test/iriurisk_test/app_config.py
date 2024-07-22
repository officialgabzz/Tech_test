from dotenv import dotenv_values
from pydantic import BaseModel
from functools import lru_cache


class AppConfig(BaseModel):
    """
    Application config class
    """

    log_level: str = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = 8002
    api_reload: bool = True
    gpt_model: str = "gpt-3.5-turbo"
    gpt_temperature: float = 0.5
    gpt_api_key: str = ""
    gpt_max_retries: int = 3


@lru_cache
def get_config() -> AppConfig:
    """
    Load environment config
    """

    params = dotenv_values()
    return AppConfig(**params)
