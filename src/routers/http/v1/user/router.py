from fastapi import APIRouter

from .mapper import UserResponseMapper
from src.di.dependency_injection import injector
from src.usecases import user as user_ucase
from src.di.unit_of_work import AbstractUnitOfWork

UserRouter = APIRouter(prefix="/v1/user", tags=["User"])


@UserRouter.get("/")
async def get_all_users(
    page: int = 0,
    size: int = 50,
):
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
async def get_user():
    ...

@UserRouter.post("/")
async def create_user():
    ...

@UserRouter.patch("/")
async def update_user():
    ...  

@UserRouter.post("/remove")
async def remove_user():
    ...