from injector import Injector, Module, provider
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.database import IS_RELATIONAL_DB
from src.repositories.auth.repository import AuthRepository
from src.repositories.refresh_token.repository import RefreshTokenRepository
from src.repositories.user.repository import UserRepository
from .unit_of_work import (
    AbstractUnitOfWork,
    AsyncSQLAlchemyUnitOfWork,
)


class RelationalDBModule(Module):
    @provider
    def provide_async_session(self) -> AsyncSession:
        from src.configs.database import get_async_session

        return get_async_session()

    @provider
    def provide_auth_repository(self, session: AsyncSession) -> AuthRepository:
        return AuthRepository(session)

    @provider
    def provide_refresh_token_repository(self, session: AsyncSession) -> RefreshTokenRepository:
        return RefreshTokenRepository(session)
    
    @provider
    def provide_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(session)

    @provider
    def provide_async_sqlalchemy_unit_of_work(
        self,
        session: AsyncSession,
        auth_repo: AuthRepository,
        refresh_token_repo: RefreshTokenRepository,
        user_repo: UserRepository,
    ) -> AbstractUnitOfWork:
        return AsyncSQLAlchemyUnitOfWork(session, auth_repo, refresh_token_repo, user_repo)


class DatabaseModuleFactory:
    def create_module(self):
        if IS_RELATIONAL_DB:
            return RelationalDBModule()

injector = Injector([DatabaseModuleFactory().create_module()])
