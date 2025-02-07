import abc
from typing import Any
from uuid import UUID

from src.models.auth import AuthModel


class AbstractAuthRepository(abc.ABC):
    session: Any

    @abc.abstractmethod
    async def get_by_id(self, id: UUID):
        raise NotImplementedError
       
    @abc.abstractmethod
    async def get_by_email(self, email: str):
        raise NotImplementedError

    # @abc.abstractmethod
    # async def list(self, params: GetPokemonParamsModel | None = None) -> list[PokemonModel]:
    #     raise NotImplementedError

    @abc.abstractmethod
    async def create(self, data: AuthModel) -> UUID:
        raise NotImplementedError

    # @abc.abstractmethod
    # async def update(self, id: UUID, data: UpdatePokemonModel):
    #     raise NotImplementedError

    # @abc.abstractmethod
    # async def delete(self, id: UUID):
    #     raise NotImplementedError

    # @abc.abstractmethod
    # async def is_existed(self, ids: list[UUID]) -> bool:
    #     raise NotImplementedError