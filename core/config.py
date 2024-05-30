from pathlib import Path
from pydantic.v1 import BaseSettings, BaseModel

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15

class Settings(BaseSettings):
    db_url: str = f"postgresql+asyncpg://postgres:postgres@db:5432/TestFAapp"
    db_echo: bool = True
    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()
