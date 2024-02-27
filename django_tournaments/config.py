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


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    secret_key: SecretStr = (
        "django-insecure-=cldztbc4jg&xl0!x673!*v2_=p$$eu)=7*f#d0#zs$44xx-h^"
    )
    database: DatabaseSettings
    google: GoogleProviderSettings


env = Environment()
