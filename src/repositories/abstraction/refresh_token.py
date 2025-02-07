import abc
from typing import Any
from uuid import UUID

from src.models.auth import AuthModel


class AbstractRefreshTokenRepository(abc.ABC):
    session: Any