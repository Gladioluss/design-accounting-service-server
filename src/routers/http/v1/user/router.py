from uuid import UUID
from fastapi import APIRouter, Path

from src.routers.http.v1.user.schema import GetAllUsersResponseModel, UserResponseModel

from .mapper import UserResponseMapper
from src.di.dependency_injection import injector
from src.usecases import user as user_ucase
from src.di.unit_of_work import AbstractUnitOfWork

UserRouter = APIRouter(prefix="/v1/user", tags=["User"])


@UserRouter.get("/")
async def _get_all_users(
    page: int = 0,
    size: int = 50,
) -> GetAllUsersResponseModel:
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    users, next_count = await user_ucase.get_all_users(
        async_unit_of_work=async_unit_of_work,
        page=page, 
        size=size
    )
    return UserResponseMapper.get_all_users_to_response(
        instance=users,
        page=page,
        size=size,
        next_count=next_count
    )


@UserRouter.get("/{id}")
async def _get_user(
    id: UUID = Path(...)
) -> UserResponseModel:
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    user = await user_ucase.get_user(
        async_unit_of_work=async_unit_of_work,
        id=id
    )
    return UserResponseMapper.user_to_response(
        instance=user
    )


@UserRouter.post("/")
async def _create_user(): ...


@UserRouter.patch("/")
async def _update_user(): ...  


@UserRouter.post("/remove")
async def _remove_user(): ...