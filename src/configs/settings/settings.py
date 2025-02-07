from functools import lru_cache
from typing import Any

from pydantic import AnyHttpUrl, PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_PREFIX: str = "/api"
    API_TITLE: str
    APP_PORT: int | str
    CORS_ORIGINS: list[str] | list[AnyHttpUrl]

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int | str
    DATABASE_NAME: str

    SQLALCHEMY_ECHO: bool
    SQLALCHEMY_ISOLATION_LEVEL: str
    DB_POOL_SIZE: int = 90
    ASYNC_DATABASE_URI: PostgresDsn | None = None

    SECRET_KEY: bytes

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str


    @field_validator("ASYNC_DATABASE_URI")
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> Any:

        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("DATABASE_USER"),
            password=values.data.get("DATABASE_PASSWORD"),
            host=values.data.get("DATABASE_HOST"),
            port=int(values.data.get("DATABASE_PORT")),
            path=f"{values.data.get('DATABASE_NAME') or ''}",
        )

    class Config:
        env_file = ".env"
        case_sensitive = True
        validate_assignment = True

@lru_cache
def get_environment_variables():
    return EnvironmentSettings()


settings = get_environment_variables()
