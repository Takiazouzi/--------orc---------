from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "Smart Document AI"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/document_ai"

settings = Settings()
