import abc
from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.abstraction.auth import AbstractAuthRepository
from src.repositories.auth.repository import AuthRepository

# pylint: disable=import-outside-toplevel,attribute-defined-outside-init


TAuth = TypeVar('TAuth', bound=AbstractAuthRepository)


class AbstractUnitOfWork(Generic[TAuth], ABC):
    auth_repo: AbstractAuthRepository

    def __init__(self, auth_repo: TAuth):
        self.auth_repo = auth_repo

    @abstractmethod
    async def __aenter__(self) -> 'AbstractUnitOfWork[TAuth]':
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError


class AsyncSQLAlchemyUnitOfWork(AbstractUnitOfWork[AuthRepository]):
    def __init__(self, session: AsyncSession, auth_repo: AuthRepository):
        super().__init__(auth_repo)
        self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(
        self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: Any
    ):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()
            await self.remove()

    async def remove(self):
        from src.configs.database import AsyncScopedSession

        await AsyncScopedSession.remove()


