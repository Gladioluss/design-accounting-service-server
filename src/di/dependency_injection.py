from injector import Injector, Module, provider
from sqlalchemy.ext.asyncio import AsyncSession
from src.configs.database import IS_RELATIONAL_DB
from src.repositories.auth.repository import AuthRepository
from src.repositories.check_measurement.repository import CheckMeasurementRepository
from src.repositories.construction.repository import ConstructionRepository
from src.repositories.defect.repository import DefectRepository
from src.repositories.refresh_token.repository import RefreshTokenRepository
from src.repositories.stage_check.repository import StageCheckRepository
from src.repositories.task.repository import TaskRepository
from src.repositories.user.repository import UserRepository
from src.repositories.work_type.repository import WorkTypeRepository

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
    def provide_check_measurement_repository(self, session: AsyncSession) -> CheckMeasurementRepository:
        return CheckMeasurementRepository(session)

    @provider
    def provide_construction_repository(self, session: AsyncSession) -> ConstructionRepository:
        return ConstructionRepository(session)

    @provider
    def provide_defect_repository(self, session: AsyncSession) -> DefectRepository:
        return DefectRepository(session)

    @provider
    def provide_refresh_token_repository(self, session: AsyncSession) -> RefreshTokenRepository:
        return RefreshTokenRepository(session)

    @provider
    def provide_stage_check_repository(self, session: AsyncSession) -> StageCheckRepository:
        return StageCheckRepository(session)

    @provider
    def provide_task_repository(self, session: AsyncSession) -> TaskRepository:
        return TaskRepository(session)

    @provider
    def provide_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(session)

    @provider
    def provide_work_type_repository(self, session: AsyncSession) -> WorkTypeRepository:
        return WorkTypeRepository(session)


    @provider
    def provide_async_sqlalchemy_unit_of_work(
        self,
        session: AsyncSession,
        auth_repo: AuthRepository,
        check_measurement_repo: CheckMeasurementRepository,
        construction_repo: ConstructionRepository,
        defect_repo: DefectRepository,
        refresh_token_repo: RefreshTokenRepository,
        stage_check_repo: StageCheckRepository,
        task_repo: TaskRepository,
        user_repo: UserRepository,
        work_type_repo: WorkTypeRepository,
    ) -> AbstractUnitOfWork:
        return AsyncSQLAlchemyUnitOfWork(
            session=session,
            auth_repo=auth_repo,
            check_measurement_repo=check_measurement_repo,
            construction_repo=construction_repo,
            defect_repo=defect_repo,
            refresh_token_repo=refresh_token_repo,
            stage_check_repo=stage_check_repo,
            task_repo=task_repo,
            user_repo=user_repo,
            work_type_repo=work_type_repo,
)


class DatabaseModuleFactory:
    def create_module(self):
        if IS_RELATIONAL_DB:
            return RelationalDBModule()

injector = Injector([DatabaseModuleFactory().create_module()])
