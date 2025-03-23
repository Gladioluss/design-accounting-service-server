from uuid import UUID

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.refresh_token import RefreshToken
from src.models.refresh_token import RefreshTokenModel
from src.repositories.abstraction.refresh_token import AbstractRefreshTokenRepository


class RefreshTokenRepository(AbstractRefreshTokenRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> RefreshTokenModel | None:
        stmt = (
            select(RefreshToken)
            .where(RefreshToken.c.id == id)
        )
        refresh_token = (await self.session.execute(stmt)).scalars().one_or_none()
        return refresh_token

    async def get_by_user_id(self, user_id: UUID) -> RefreshTokenModel | None:
        stmt = (
            select(RefreshToken)
            .where(RefreshToken.c.user_id == user_id)
        )
        refresh_token = (await self.session.execute(stmt)).scalars().one_or_none()
        return refresh_token

    async def create(self, data: RefreshTokenModel) -> None:
        stmt = insert(RefreshToken).values(
            user_id=data.user_id,
            refresh_token=data.refresh_token,
        )
        await self.session.execute(stmt)
