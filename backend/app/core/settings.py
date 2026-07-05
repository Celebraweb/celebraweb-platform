from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    Configuración centralizada de CelebraWeb Platform.
    Toda la plataforma debe obtener la configuración desde aquí.
    """

    # Platform
    APP_NAME: str = "CelebraWeb Platform"
    APP_VERSION: str = "0.2.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str

    # JWT
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


@lru_cache
def get_settings() -> Settings:
    """
    Devuelve una única instancia de Settings durante
    toda la ejecución de la aplicación.
    """
    return Settings()


settings = get_settings()