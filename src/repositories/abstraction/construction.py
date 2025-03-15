import abc
from typing import Any
from uuid import UUID


class AbstractConstructionRepository(abc.ABC):
    session: Any
