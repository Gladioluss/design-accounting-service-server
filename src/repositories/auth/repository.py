from datetime import datetime
from typing import Callable
from uuid import UUID

from sqlalchemy import Boolean, Column, DateTime, String, insert, table, select
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.uuid import uuid7
from src.models.auth import AuthModel
from src.repositories.abstraction.auth import AbstractAuthRepository
from src.utils.verification.generate_verify_token import generate_verification_token

func: Callable

user_table = table(
    "user", 
    Column("id", SQLUUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("middle_name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("verify_token", String(255)),
    Column("updated_at", DateTime),
    Column("created_at", DateTime),
    Column("is_admin", Boolean),
    Column("is_verify", Boolean),
    Column("is_deleted", Boolean)
)

class AuthRepository(AbstractAuthRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> AuthModel | None:
        stmt = (
            select(user_table)
            .where(user_table.c.id == id)
        )
        user = (await self.session.execute(stmt)).mappings().one_or_none()
        return user

    async def get_by_email(self, email: str) -> AuthModel | None:
        stmt = (
            select(user_table)
            .where(user_table.c.email == email)
        )
        user = (await self.session.execute(stmt)).mappings().one_or_none()
        return user
    
    async def create(self, data: AuthModel) -> None:
        stmt = insert(user_table).values(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            email=data.email,
            password=data.password,
            verify_token=generate_verification_token(),
            updated_at=datetime.now(),
            created_at=datetime.now(),
            is_admin=True,
            is_verify=False,
            is_deleted=False
        )
        await self.session.execute(stmt)
    