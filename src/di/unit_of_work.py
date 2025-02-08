import abc
from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.abstraction.refresh_token import AbstractRefreshTokenRepository
from src.repositories.refresh_token.repository import RefreshTokenRepository
from src.repositories.abstraction.auth import AbstractAuthRepository
from src.repositories.auth.repository import AuthRepository

# pylint: disable=import-outside-toplevel,attribute-defined-outside-init



class AbstractUnitOfWork(ABC):
    auth_repo: AbstractAuthRepository
    refresh_token_repo: AbstractRefreshTokenRepository

    def __init__(
        self, 
        auth_repo: AbstractAuthRepository,
        refresh_token_repo: AbstractRefreshTokenRepository
    ):
        self.auth_repo = auth_repo
        self.refresh_token_repo=refresh_token_repo

    @abstractmethod
    async def __aenter__(self) -> 'AbstractUnitOfWork':
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError


class AsyncSQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(
            self, 
            session: AsyncSession, 
            auth_repo: AuthRepository,
            refresh_token_repo: RefreshTokenRepository
        ):
        super().__init__(auth_repo, refresh_token_repo)
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




# import abc
# from abc import ABC, abstractmethod
# from typing import Any, Generic, Type, TypeVar

# from sqlalchemy.ext.asyncio import AsyncSession

# from src.repositories.abstraction.refresh_token import AbstractRefreshTokenRepository
# from src.repositories.refresh_token.repository import RefreshTokenRepository
# from src.repositories.abstraction.auth import AbstractAuthRepository
# from src.repositories.auth.repository import AuthRepository

# # pylint: disable=import-outside-toplevel,attribute-defined-outside-init


# TAuth = TypeVar('TAuth', bound=AbstractAuthRepository)
# TRefreshToken = TypeVar('TRefreshToken', bound=AbstractRefreshTokenRepository)

# class AbstractUnitOfWork(Generic[TAuth], Generic[TRefreshToken], ABC):
#     auth_repo: AbstractAuthRepository
#     refresh_token_repo: AbstractRefreshTokenRepository

#     def __init__(
#         self, 
#         auth_repo: TAuth,
#         refresh_token_repo: TRefreshToken
#     ):
#         self.auth_repo = auth_repo
#         self.refresh_token_repo=refresh_token_repo

#     @abstractmethod
#     async def __aenter__(self) -> 'AbstractUnitOfWork[TAuth]':
#         raise NotImplementedError
    
#     @abstractmethod
#     async def __aenter__(self) -> 'AbstractUnitOfWork[TRefreshToken]':
#         raise NotImplementedError

#     @abstractmethod
#     async def __aexit__(self, exc_type, exc, tb):
#         raise NotImplementedError


# class AsyncSQLAlchemyUnitOfWork(AbstractUnitOfWork[AuthRepository], AbstractUnitOfWork[RefreshTokenRepository]):
#     def __init__(
#             self, 
#             session: AsyncSession, 
#             auth_repo: AuthRepository,
#             refresh_token_repo: RefreshTokenRepository
#         ):
#         super().__init__(auth_repo, refresh_token_repo)
#         self._session = session

#     async def __aenter__(self):
#         return self

#     async def __aexit__(
#         self, exc_type: Type[BaseException] | None, exc: BaseException | None, tb: Any
#     ):
#         try:
#             if exc_type is None:
#                 await self._session.commit()
#             else:
#                 await self._session.rollback()
#         finally:
#             await self._session.close()
#             await self.remove()

#     async def remove(self):
#         from src.configs.database import AsyncScopedSession

#         await AsyncScopedSession.remove()


