"""
Application configuration.

Loads environment variables from .env
and makes them available throughout the project.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "gemma2-9b-it"

    class Config:
        env_file = ".env"


settings = Settings()