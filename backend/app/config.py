from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = Field(default="development", alias="APP_ENV")
    database_url: str = Field(
        default="postgresql://postgres:postgres@db:5432/interview",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://redis:6379/0", alias="REDIS_URL")
    sql_echo: bool = Field(default=False, alias="SQL_ECHO")
    ws_session_ttl_seconds: int = Field(default=3600, alias="WS_SESSION_TTL_SECONDS")
    ws_rate_limit_max: int = Field(default=20, alias="WS_RATE_LIMIT_MAX")
    ws_rate_limit_window_seconds: int = Field(
        default=60,
        alias="WS_RATE_LIMIT_WINDOW_SECONDS",
    )


settings = Settings()
