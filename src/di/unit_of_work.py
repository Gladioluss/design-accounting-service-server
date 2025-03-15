from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.auth import AbstractAuthRepository
from src.repositories.abstraction.check_measurement import AbstractCheckMeasurementRepository
from src.repositories.abstraction.construction import AbstractConstructionRepository
from src.repositories.abstraction.defect import AbstractDefectRepository
from src.repositories.abstraction.refresh_token import AbstractRefreshTokenRepository
from src.repositories.abstraction.stage_check import AbstractStageCheckRepository
from src.repositories.abstraction.task import AbstractTaskRepository
from src.repositories.abstraction.user import AbstractUserRepository
from src.repositories.abstraction.work_type import AbstractWorkTypeRepository
from src.repositories.auth.repository import AuthRepository
from src.repositories.check_measurement.repository import CheckMeasurementRepository
from src.repositories.construction.repository import ConstructionRepository
from src.repositories.defect.repository import DefectRepository
from src.repositories.refresh_token.repository import RefreshTokenRepository
from src.repositories.stage_check.repository import StageCheckRepository
from src.repositories.task.repository import TaskRepository
from src.repositories.user.repository import UserRepository
from src.repositories.work_type.repository import WorkTypeRepository


class AbstractUnitOfWork(ABC):
    auth_repo: AbstractAuthRepository
    check_measurement_repo: AbstractCheckMeasurementRepository
    construction_repo: AbstractConstructionRepository
    defect_repo: AbstractDefectRepository
    refresh_token_repo: AbstractRefreshTokenRepository
    stage_check_repo: AbstractStageCheckRepository
    task_repo: AbstractTaskRepository
    user_repo: AbstractUserRepository
    work_type_repo: AbstractWorkTypeRepository

    def __init__(
        self,
        auth_repo: AbstractAuthRepository,
        check_measurement_repo: AbstractCheckMeasurementRepository,
        construction_repo: AbstractConstructionRepository,
        defect_repo: AbstractDefectRepository,
        refresh_token_repo: AbstractRefreshTokenRepository,
        stage_check_repo: AbstractStageCheckRepository,
        task_repo: AbstractTaskRepository,
        user_repo: AbstractUserRepository,
        work_type_repo: AbstractWorkTypeRepository,
    ):
        self.auth_repo = auth_repo
        self.check_measurement_repo = check_measurement_repo
        self.construction_repo = construction_repo
        self.defect_repo = defect_repo
        self.refresh_token_repo=refresh_token_repo
        self.stage_check_repo = stage_check_repo
        self.task_repo = task_repo
        self.user_repo=user_repo
        self.work_type_repo=work_type_repo

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
            check_measurement_repo: CheckMeasurementRepository,
            construction_repo: ConstructionRepository,
            defect_repo: DefectRepository,
            refresh_token_repo: RefreshTokenRepository,
            stage_check_repo: StageCheckRepository,
            task_repo: TaskRepository,
            user_repo: UserRepository,
            work_type_repo: WorkTypeRepository,
        ):
        super().__init__(
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
        self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: Any
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
