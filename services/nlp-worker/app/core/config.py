from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://smartdoc_user:smartdoc_pass@postgres:5432/smartdoc_db")

    class Config:
        env_file = ".env"

settings = Settings()
