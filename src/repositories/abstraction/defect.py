import abc
from typing import Any
from uuid import UUID


class AbstractDefectRepository(abc.ABC):
    session: Any
