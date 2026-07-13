from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "YaSara"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str = "postgresql+asyncpg://yasara:yasara@localhost:5432/yasara"
    SQLITE_DATABASE_URL: str = "sqlite+aiosqlite:///./yasara_dev.db"
    USE_SQLITE: bool = False

    JWT_SECRET_KEY: str = "change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    BINANCE_FUTURES_REST_URL: str = "https://fapi.binance.com"
    BITUNIX_FUTURES_REST_URL: str = "https://fapi.bitunix.com"

    LOG_LEVEL: str = "INFO"

    BASE_DIR: Path = Path(__file__).resolve().parents[3]
    DATA_DIR: Path = BASE_DIR / "data"
    LOG_DIR: Path = BASE_DIR / "logs"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    @property
    def database_url(self) -> str:
        return self.SQLITE_DATABASE_URL if self.USE_SQLITE else self.DATABASE_URL

    def ensure_directories(self) -> None:
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.ensure_directories()
    return settings


settings = get_settings()
