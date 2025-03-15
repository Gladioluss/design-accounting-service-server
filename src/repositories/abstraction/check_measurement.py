import abc
from typing import Any
from uuid import UUID


class AbstractCheckMeasurementRepository(abc.ABC):
    session: Any
