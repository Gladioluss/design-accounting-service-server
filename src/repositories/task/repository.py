from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.task import AbstractTaskRepository


class TaskRepository(AbstractTaskRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
