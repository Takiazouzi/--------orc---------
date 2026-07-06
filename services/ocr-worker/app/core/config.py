from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    class Config:
        env_file = ".env"

settings = Settings()
