from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, and_, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as SQLUUID

from src.models.user import UserModel
from src.repositories.auth.repository import user_table
from src.repositories.abstraction.user import AbstractUserRepository
from src.utils.uuid import uuid7

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(SQLUUID(as_uuid=True), primary_key=True, default=uuid7)
#     first_name = Column(String)
#     last_name = Column(String)
#     middle_name = Column(String)
#     email = Column(String)
#     password = Column(String)
#     updated_at = Column(DateTime, default=datetime.now())
#     created_at = Column(DateTime, default=datetime.now())
#     is_admin = Column(Boolean)
#     is_verify = Column(Boolean)
#     is_deleted = Column(Boolean)


class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_users(self, limit: int, offset: int) -> tuple[list[UserModel], int]:
        stmt = (
            select(user_table)
            .offset(offset)
            .limit(limit)
            .where(
                and_(
                    user_table.c.is_verify == True,
                    user_table.c.is_deleted == False
                )
            )
        )
        users = (await self.session.execute(stmt)).mappings().all()
        
        next_offset = offset + limit
        next_stmt = (
            select(user_table.c.id)
            .offset(next_offset)
            .limit(limit)
            .where(
                and_(
                    user_table.c.is_verify == True,
                    user_table.c.is_deleted == False
                )
            )
        )
        next_count = (await self.session.execute(func.count(next_stmt))).scalar()

        return users, next_count