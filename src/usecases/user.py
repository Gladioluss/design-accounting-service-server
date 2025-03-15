from uuid import UUID

from src.configs.security.security import encrypt_password
from src.di.unit_of_work import AbstractUnitOfWork
from src.errors.auth import UserAlreadyExists, UserNotFoundError
from src.models.user import UserModel


async def get_all_users(
    async_unit_of_work: AbstractUnitOfWork,
    page: int,
    size: int,
) -> tuple[list[UserModel], int]:
    async with async_unit_of_work as auow:
        offset = page * size
        users, next_count = await auow.user_repo.get_all(limit=size, offset=offset)
        return users, next_count

async def get_user(
    async_unit_of_work: AbstractUnitOfWork,
    id: UUID
) -> UserModel:
    async with async_unit_of_work as auow:
        user = await auow.user_repo.get_by_id(id=id)

        if user is None:
            raise UserNotFoundError(id)
        return user

async def create_user(
    async_unit_of_work: AbstractUnitOfWork,
    data: UserModel
):
    async with async_unit_of_work as auow:
        user = await auow.auth_repo.get_by_email(email=data.email)

        if user:
            raise UserAlreadyExists(data.email)

        data.password = encrypt_password(password=data.password)
        await auow.user_repo.create(
            data=data
        )
