import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Marketing Tool"
    API_V1_STR: str = "/api/v1"
    
    # SECURITY
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"  # JWT algorithm
    
    # POSTGRESQL
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "")
    
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
    @property
    def get_database_uri(self) -> str:
        """Construct database URI from components."""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # EXTERNAL APIS
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DIALOGFLOW_PROJECT_ID: str = os.getenv("DIALOGFLOW_PROJECT_ID", "")
    BUFFER_API_KEY: str = os.getenv("BUFFER_API_KEY", "")
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000", 
        "http://localhost:8000",
        # Add more frontend origins as needed
        "*"  # This allows any origin - for development only, remove in production!
    ]
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
settings.SQLALCHEMY_DATABASE_URI = settings.get_database_uri



