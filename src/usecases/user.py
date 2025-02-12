from src.models.user import UserModel
from src.di.unit_of_work import AbstractUnitOfWork


async def get_all_users(
    async_unit_of_work: AbstractUnitOfWork,
    page: int,
    size: int,
) -> tuple[list[UserModel], int]:
    async with async_unit_of_work as auow:
        offset = page * size
        users, next_count = await auow.user_repo.get_all_users(limit=size, offset=offset)
        return users, next_count