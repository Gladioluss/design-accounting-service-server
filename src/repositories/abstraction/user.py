import abc
from typing import Any
from uuid import UUID

from src.models.user import UpdateUserModel, UserModel


class AbstractUserRepository(abc.ABC):
    session: Any


    @abc.abstractmethod
    async def get_all(self, limit: int, offset: int) -> tuple[list[UserModel], int]:
        raise NotImplementedError
    

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> UserModel | None:
        raise NotImplementedError
    

    @abc.abstractmethod
    async def create(self, id: UUID, data: UserModel) -> UserModel:
        raise NotImplementedError


    @abc.abstractmethod
    async def update(self, id: UUID, data: UpdateUserModel) -> UserModel:
        raise NotImplementedError