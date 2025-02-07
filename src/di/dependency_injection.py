from injector import Injector, Module, provider
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.database import IS_RELATIONAL_DB
from src.repositories.auth.repository import AuthRepository

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
    def provide_async_sqlalchemy_unit_of_work(
        self, 
        session: AsyncSession, 
        auth_repo: AuthRepository
    ) -> AbstractUnitOfWork:
        return AsyncSQLAlchemyUnitOfWork(session, auth_repo)


class DatabaseModuleFactory:
    def create_module(self):
        if IS_RELATIONAL_DB:
            return RelationalDBModule()

injector = Injector([DatabaseModuleFactory().create_module()])