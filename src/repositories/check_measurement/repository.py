from uuid import UUID

from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.abstraction.check_measurement import AbstractCheckMeasurementRepository


class CheckMeasurementRepository(AbstractCheckMeasurementRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
