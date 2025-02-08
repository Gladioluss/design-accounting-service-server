import abc
from typing import Any
from uuid import UUID

from src.models.auth import AuthModel


class AbstractAuthRepository(abc.ABC):
    session: Any

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> AuthModel | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_email(self, email: str) -> AuthModel | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_verify_token_by_user_email(self, email: str) -> str | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def verify_user_by_user_email(self, email: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, data: AuthModel) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def update_verify_token_by_user_email(self, email: str, verify_token: str) -> str | None:
        raise NotImplementedError
