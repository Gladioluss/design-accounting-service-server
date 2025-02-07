from datetime import datetime, timedelta
from enum import Enum
from typing import Any

import jwt
from jwt import DecodeError, ExpiredSignatureError, MissingRequiredClaimError
from passlib.context import CryptContext

from src.errors.token import (
    TokenExpiredSignatureError,
    TokenDecodeError,
    TokenMissingRequiredClaimError
)
from src.configs.settings.settings import settings


class TokenType(str, Enum):
    refresh_token = "refresh_token"
    access_token = "access_token"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, encrypted_password: str):
    return pwd_context.verify(password, encrypted_password)


def create_access_token(subject: str | Any) -> str:
    expire = datetime.now() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"exp": expire, "sub": str(subject), "type": TokenType.access_token}

    return jwt.encode(
        payload=to_encode,
        key=settings.ENCRYPT_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_refresh_token(subject: str | Any) -> str:
    expire = datetime.now() + timedelta(
        minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"exp": expire, "sub": str(subject), "type": TokenType.refresh_token}

    return jwt.encode(
        payload=to_encode,
        key=settings.ENCRYPT_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            jwt=token,
            key=settings.ENCRYPT_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
    except ExpiredSignatureError as e:
        raise TokenExpiredSignatureError() from e
    except DecodeError as e:
        raise TokenDecodeError() from e
    except MissingRequiredClaimError as e:
        raise TokenMissingRequiredClaimError() from e