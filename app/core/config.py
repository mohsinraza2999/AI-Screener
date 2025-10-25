from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_TYPE: str = "gpt-4"

    class Config:
        env_file = ".env"

settings = Settings()
