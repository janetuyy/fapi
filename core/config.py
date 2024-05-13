from pathlib import Path
from pydantic.v1 import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = f"postgresql://postgres:postgres@localhost:5432/TestFAapp"
    db_echo: bool = True


settings = Settings()
