import abc
from typing import Any


class AbstractConstructionRepository(abc.ABC):
    session: Any
