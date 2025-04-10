from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.defect import AbstractDefectRepository


class DefectRepository(AbstractDefectRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
