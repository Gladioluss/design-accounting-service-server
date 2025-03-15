from uuid import UUID

from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.entities.user import User
from src.models.auth import AuthModel
from src.repositories.abstraction.auth import AbstractAuthRepository
from src.utils.verification.generate_verify_token import generate_verification_token


class AuthRepository(AbstractAuthRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> AuthModel | None:
        stmt = (
            select(User)
            .where(User.c.id == id)
        )
        user = (await self.session.execute(stmt)).mappings().one_or_none()
        return user

    async def get_by_email(self, email: str) -> AuthModel | None:
        stmt = (
            select(User)
            .where(User.c.email == email)
        )
        user = (await self.session.execute(stmt)).mappings().one_or_none()
        return user


    async def get_verify_token_by_user_email(self, email: str) -> str | None:
        stmt = (
            select(User.c.verify_token)
            .where(
                and_(
                    User.c.email == email,
                    User.c.is_deleted == False
                )
            )
        )
        verify_token = (await self.session.execute(stmt)).scalar_one_or_none()
        return verify_token

    async def verify_user_by_user_email(self, email: str) -> None:
        stmt = (
            update(User)
            .where(User.c.email == email)
            .values(is_verify=True)
        )
        await self.session.execute(stmt)


    async def create(self, data: AuthModel) -> None:
        stmt = insert(User).values(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            email=data.email,
            password=data.password,
            verify_token=await generate_verification_token(),
            is_admin=True,
            is_verify=False,
            is_deleted=False
        )
        await self.session.execute(stmt)

    async def update_verify_token_by_user_email(self, email: str, verify_token: str) -> str | None:
        stmt = (
            update(User)
            .where(User.c.email == email)
            .values(verify_token=verify_token,)
            .returning(User.c.verify_token)
        )
        verify_token = (await self.session.execute(stmt)).scalar_one_or_none()
        return verify_token
