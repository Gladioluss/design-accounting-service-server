from fastapi import Depends
from sqlmodel import select, func

from app.configs.database.postgresql.database import get_db_connection
from sqlmodel.ext.asyncio.session import AsyncSession

from app.entities.user import User
from app.models.user import UserModel, user_entity_to_model

class UserRepository:
    db: AsyncSession

    def __init__(
        self, db: AsyncSession = Depends(get_db_connection)
    ) -> None:
        self.db = db
    
    async def get_user_by_id(
            self, 
            user_id
    ) -> UserModel:
        return await self.db.exec(select(User).where(User.id == user_id))
    
    async def get_all_users(
        self,
        limit: int,
        start: int,
    ) -> list[UserModel]:
        result = (await self.db.exec(select(User).offset(start).limit(limit).where(User.is_deleted != True))).all()
        return [user_entity_to_model(user) for user in result]
    
    async def get_total_count(
        self
    ) -> int:
        result = await self.db.exec(select(func.count()).select_from(select(User).subquery()))
        return result.one()
    
    async def create_user(
        self, 
        user: UserModel
    ) -> UserModel:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    