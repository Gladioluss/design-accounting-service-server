from uuid import UUID

from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.work_type import WorkType
from src.models.work_type import WorkTypeModel
from src.repositories.abstraction.work_type import AbstractWorkTypeRepository


class WorkTypeRepository(AbstractWorkTypeRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> WorkTypeModel | None:
        stmt = (
            select(WorkType)
            .where(WorkType.c.id == id)
        )
        work_type = (await self.session.execute(stmt)).mappings().one_or_none()
        return work_type

    async def get_by_name(self, name: str) -> WorkTypeModel | None:
        stmt = (
            select(WorkType)
            .where(WorkType.c.name == name)
        )
        work_type = (await self.session.execute(stmt)).mappings().one_or_none()
        return work_type


    async def create(self, data: WorkTypeModel) -> None:
        stmt = insert(WorkType).values(
            name=data.name,
        )
        await self.session.execute(stmt)
