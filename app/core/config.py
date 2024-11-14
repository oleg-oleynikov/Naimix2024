import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REST_PORT: int = 8000
    SWISSEPH_PATH: str = ""
    DATABASE_URL: str = ""
    SWAGGER_SYNTAX_HIGHLIGHT: bool = False

    class Config:
        env_file = ".env"

settings = Settings()