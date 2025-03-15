from uuid import UUID

from fastapi import APIRouter, Depends, Path
from src.di.dependency_injection import injector
from src.di.unit_of_work import AbstractUnitOfWork
from src.usecases import work_type as work_type_ucase
from src.utils.authorization import authorization

from .mapper import WorkTypeRequestMapper
from .schema import CreateWorkTypeRequest

WorkTypeRouter = APIRouter(prefix="/work_type", tags=["WorkType"])


@WorkTypeRouter.get("/")
async def _get_all_work_types(
    token: str = Depends(authorization)
): ...


@WorkTypeRouter.get("/{id}")
async def _get_work_type_by_id(
    id: UUID = Path(...),
    token: str = Depends(authorization)
): ...

@WorkTypeRouter.post("/")
async def _create_work_type(
    body: CreateWorkTypeRequest,
    token: str = Depends(authorization)
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    user_data = WorkTypeRequestMapper.create_work_type_request_to_model(instance=body)
    await work_type_ucase.create_work_type(
        async_unit_of_work=async_unit_of_work,
        data=user_data
    )


@WorkTypeRouter.patch("/")
async def _update_work_type(
    token: str = Depends(authorization)
): ...


@WorkTypeRouter.post("/remove/{id}")
async def _remove_work_type(
    id: UUID = Path(...),
    token: str = Depends(authorization)
): ...
