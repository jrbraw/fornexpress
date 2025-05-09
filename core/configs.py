import os
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação.
    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str
    PROJECT_NAME: str = "Api de serviços Fornexpress"

    BASE_DIR: Path = os.path.dirname(os.path.abspath(__name__))
    UPLOAD_DIR: Path = os.path.join(BASE_DIR, "uploads")
    TEMPLATE_DIR: Path = os.path.join(BASE_DIR, "templates")

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
