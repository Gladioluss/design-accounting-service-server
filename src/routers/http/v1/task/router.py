from uuid import UUID

from fastapi import APIRouter, Path

TaskRouter = APIRouter(prefix="/task", tags=["Task"])

@TaskRouter.get("/")
async def _get_all_tasks(): ...


@TaskRouter.get("/{id}")
async def _get_task_by_id(
    id: UUID = Path(...)
): ...

@TaskRouter.post("/")
async def _create_task(): ...


@TaskRouter.patch("/")
async def _update_task(): ...

@TaskRouter.post("/remove/{id}")
async def _remove_tsak(
    id: UUID = Path(...)
): ...