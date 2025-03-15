from uuid import UUID

from fastapi import APIRouter, Depends, Path
from src.utils.authorization import authorization

TaskRouter = APIRouter(prefix="/task", tags=["Task"])

@TaskRouter.get("/")
async def _get_all_tasks(
    token: str = Depends(authorization)
): ...


@TaskRouter.get("/{id}")
async def _get_task_by_id(
    id: UUID = Path(...),
    token: str = Depends(authorization)
): ...

@TaskRouter.post("/")
async def _create_task(
    token: str = Depends(authorization)
): ...


@TaskRouter.patch("/")
async def _update_task(
    token: str = Depends(authorization)
): ...

@TaskRouter.post("/remove/{id}")
async def _remove_tsak(
    id: UUID = Path(...),
    token: str = Depends(authorization)
): ...