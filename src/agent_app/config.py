
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"


def load_config() -> AppConfig:
    """Load app configuration from .env/environment variables."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and set your key."
        )

    return AppConfig(
        openai_api_key=api_key,
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    )
