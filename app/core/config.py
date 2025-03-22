from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
import os
from dotenv import load_dotenv

env_path = f"{os.getcwd()}/.env"
load_dotenv(env_path)


class Settings(BaseSettings):
    DATABASE_URL: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    SECRET_KEY: str
    DEBUG: bool

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
    )


try:
    settings = Settings()
except ValidationError as e:
    print(f"==>> e: {e}")
    raise ValueError(
        "Missing required environment variables. Check your .env file!"
    ) from e
