from sqlalchemy import and_, func, select
from sqlalchemy.ext.asyncio import AsyncSession


from src.entities.user import User
from src.models.user import UserModel
from src.repositories.auth.repository import User
from src.repositories.abstraction.user import AbstractUserRepository


class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_users(self, limit: int, offset: int) -> tuple[list[UserModel], int]:
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