from typing import Optional

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    user: str
    password: SecretStr
    host: str
    database: str


class GoogleProviderSettings(BaseModel):
    client_id: str
    client_secret: SecretStr


class EmailSettings(BaseModel):
    backend: str = "smtp"
    use_tls: bool = True
    host: Optional[str] = "smtp.gmail.com"
    port: Optional[int] = 587
    host_user: Optional[str] = None
    host_password: Optional[SecretStr] = None


class Environment(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )

    debug: bool = False
    secret_key: SecretStr
    database: DatabaseSettings
    google: GoogleProviderSettings
    email: EmailSettings


env = Environment()
