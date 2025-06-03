from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Snappy"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "prd"
    APP_PATH: str = "/api/v1"

    DATABASE_URL: PostgresDsn

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
    )


settings = Settings()  # type: ignore
