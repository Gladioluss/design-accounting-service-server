from uuid import UUID

from sqlalchemy import and_, func, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.user import User
from src.models.user import UpdateUserModel, UserModel
from src.repositories.abstraction.user import AbstractUserRepository
from src.repositories.auth.repository import User


class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, limit: int, offset: int) -> tuple[list[UserModel], int]:
        stmt = (
            select(User)
            .offset(offset)
            .limit(limit)
            .where(
                and_(
                    User.c.is_verify == True,
                    User.c.is_deleted == False
                )
            )
        )
        users = (await self.session.execute(stmt)).mappings().all()

        next_offset = offset + limit
        next_stmt = (
            select(User.c.id)
            .offset(next_offset)
            .limit(limit)
            .where(
                and_(
                    User.c.is_verify == True,
                    User.c.is_deleted == False
                )
            )
        )
        next_count = (await self.session.execute(func.count(next_stmt))).scalar()
        return users, next_count


    async def get_by_id(self, id: UUID) -> UserModel | None:
        stmt = (
            select(User)
            .where(
                and_(
                    User.c.id == id,
                    User.c.is_verify == True,
                    User.c.is_deleted == False
                )
            )
        )
        user = (await self.session.execute(stmt)).mappings().one_or_none()
        return user


    async def create(self, data: UserModel) -> None:
        stmt = insert(User).values(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            email=data.email,
            password=data.password,
            verify_token=None,
            is_admin=False,
            is_verify=True,
            is_deleted=False
        )
        await self.session.execute(stmt)


    async def update(self, id: UUID, data: UpdateUserModel) -> UserModel:
        raise NotImplementedError
