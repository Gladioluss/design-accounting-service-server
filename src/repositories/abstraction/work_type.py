import abc
from typing import Any
from uuid import UUID

from src.models.work_type import WorkTypeModel


class AbstractWorkTypeRepository(abc.ABC):
    session: Any

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> WorkTypeModel | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_name(self, name: str) -> WorkTypeModel | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, data: WorkTypeModel) -> None:
        raise NotImplementedError
