from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project -  Orbify"
    PROJECT_DESCRIPTION: str = "Project Manager Create, Delete, Update Projects"
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"

settings = Settings()