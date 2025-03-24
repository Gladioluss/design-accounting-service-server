from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.construction import AbstractConstructionRepository


class ConstructionRepository(AbstractConstructionRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
