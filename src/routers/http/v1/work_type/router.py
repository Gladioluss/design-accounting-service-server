from uuid import UUID

from fastapi import APIRouter, Path
from src.di.dependency_injection import injector
from src.di.unit_of_work import AbstractUnitOfWork
from src.usecases import work_type as work_type_ucase

from .mapper import WorkTypeRequestMapper
from .schema import CreateWorkTypeRequest

WorkTypeRouter = APIRouter(prefix="/work_type", tags=["WorkType"])


@WorkTypeRouter.get("/")
async def _get_all_work_types(): ...


@WorkTypeRouter.get("/{id}")
async def _get_work_type_by_id(
    id: UUID = Path(...)
): ...

@WorkTypeRouter.post("/")
async def _create_work_type(
    body: CreateWorkTypeRequest
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    user_data = WorkTypeRequestMapper.create_work_type_request_to_model(instance=body)
    await work_type_ucase.create_work_type(
        async_unit_of_work=async_unit_of_work,
        data=user_data
    )


@WorkTypeRouter.patch("/")
async def _update_work_type(): ...


@WorkTypeRouter.post("/remove/{id}")
async def _remove_work_type(
    id: UUID = Path(...)
): ...
