import abc
from typing import Any


class AbstractDefectRepository(abc.ABC):
    session: Any
