from uuid import UUID

from src.di.unit_of_work import AbstractUnitOfWork
from src.errors.work_type import WorkTypeAlreadyExists
from src.models.work_type import WorkTypeModel


async def get_by_id(
        async_unit_of_work: AbstractUnitOfWork,
        id: UUID
)-> WorkTypeModel | None:
    async with async_unit_of_work as auow:
        work_type = await auow.work_type_repo.get_by_id(name=id)
        if not work_type:
            raise
        return work_type


async def get_by_name(
        async_unit_of_work: AbstractUnitOfWork,
        name: str
)-> WorkTypeModel | None:
    async with async_unit_of_work as auow:
        work_type =  await auow.work_type_repo.get_by_name(name=name)
        if not work_type:
            raise
        return work_type

async def create_work_type(
        async_unit_of_work: AbstractUnitOfWork,
        data: WorkTypeModel
):
    async with async_unit_of_work as auow:
        work_type = await auow.work_type_repo.get_by_name(name=data.name)

        if work_type:
            raise WorkTypeAlreadyExists(data.name)

        await auow.work_type_repo.create(
            data=data
        )

