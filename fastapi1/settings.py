from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host:str = "localhost"
    server_port:int = 8000
    database_url: str = "postgresql+psycopg2://fastapi_admin:9986559@localhost:5433/fastapi_db"
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600

settings_w = Settings(
    _env_file='.env',
    _env_file_encoding = 'utf-8'
)