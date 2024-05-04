from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parent


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    ALPACA_API_KEY: str
    ALPACA_API_SECRET: str
    ALPACA_BASE_URL: str = "https://paper-api.alpaca.markets"

    @property
    def alpaca_credentials(self) -> dict:
        return {
            "API_KEY": self.ALPACA_API_KEY,
            "API_SECRET": self.ALPACA_API_SECRET,
            "PAPER": True,
        }


def _get_env_filename():
    return PROJECT_ROOT / ".env.local"


settings = AppSettings(_env_file=_get_env_filename())
