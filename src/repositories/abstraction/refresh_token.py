import abc
from typing import Any
from uuid import UUID

from src.models.refresh_token import RefreshTokenModel


class AbstractRefreshTokenRepository(abc.ABC):
    session: Any

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> RefreshTokenModel | None:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> RefreshTokenModel | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, data: RefreshTokenModel) -> None:
        raise NotImplementedError