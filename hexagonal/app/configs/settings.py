"""Settings module"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """The application settings"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DB_DSN: str
    DB_ECHO: bool = False


settings = Settings()
