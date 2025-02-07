from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, insert, table, select
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from uuid import UUID


from src.models.refresh_token import RefreshTokenModel
from src.repositories.abstraction.refresh_token import AbstractRefreshTokenRepository
from src.utils.uuid import uuid7

refresh_token_table = table(
    "refresh_token", 
    Column("id", SQLUUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("user_id", SQLUUID(as_uuid=True), ForeignKey("user.id")),
    Column("refresh_token", String(255)),
    Column("created_at", DateTime),
)

class RefreshTokenRepository(AbstractRefreshTokenRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> RefreshTokenModel | None:
        stmt = (
            select(refresh_token_table)
            .where(refresh_token_table.c.id == id)
        )
        refresh_token = (await self.session.execute(stmt)).scalars().one_or_none()
        return refresh_token
    
    async def get_by_user_id(self, user_id: UUID) -> RefreshTokenModel | None:
        stmt = (
            select(refresh_token_table)
            .where(refresh_token_table.c.user_id == user_id)
        )
        refresh_token = (await self.session.execute(stmt)).scalars().one_or_none()
        return refresh_token

    async def create(self, data: RefreshTokenModel) -> UUID:
        stmt = insert(refresh_token_table).values(
            user_id=data.user_id,
            refresh_token=data.refresh_token,
            created_at=datetime.now(),
        )
        await self.session.execute(stmt)
    