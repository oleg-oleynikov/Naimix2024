import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REST_PORT: int = 8000
    SWISSEPH_PATH: str = ""
    DATABASE_URL: str = ""
    SWAGGER_SYNTAX_HIGHLIGHT: bool = False
    KEYCLOAK_URL: str = ""
    KEYCLOAK_SECRET_KEY: str = ""
    KEYCLOAK_CLIENT_ID: str = ""
    KEYCLOAK_REALM_NAME: str = ""

    class Config:
        env_file = ".env"

def reload_settings():
    global settings
    settings = Settings()  # Переинициализирует объект, перезагружая значения из .env

# При инициализации приложения
reload_settings()
# settings = Settings()