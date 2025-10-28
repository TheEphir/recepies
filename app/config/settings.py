from pydantic_settings import BaseSettings
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")

settings = Settings()