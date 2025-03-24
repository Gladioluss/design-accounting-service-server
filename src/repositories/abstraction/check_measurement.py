import abc
from typing import Any


class AbstractCheckMeasurementRepository(abc.ABC):
    session: Any
