from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.stage_check import AbstractStageCheckRepository


class StageCheckRepository(AbstractStageCheckRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
