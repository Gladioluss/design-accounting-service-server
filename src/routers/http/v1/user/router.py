from uuid import UUID

from fastapi import APIRouter, Path, status
from src.di.dependency_injection import injector
from src.di.unit_of_work import AbstractUnitOfWork
from src.usecases import user as user_ucase

from .mapper import UserRequestMapper, UserResponseMapper
from .schema import CreateUserRequest, GetAllUsersResponseModel, UserResponseModel

UserRouter = APIRouter(prefix="/user", tags=["User"])


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


@UserRouter.post("/", status_code=status.HTTP_201_CREATED)
async def _create_user(
    body: CreateUserRequest,
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    user_data = UserRequestMapper.create_user_request_to_model(instance=body)
    await user_ucase.create_user(
        async_unit_of_work=async_unit_of_work,
        data=user_data
    )


@UserRouter.patch("/")
async def _update_user(): ...


@UserRouter.post("/remove/{id}")
async def _remove_user(
    id: UUID = Path(...)
): ...
