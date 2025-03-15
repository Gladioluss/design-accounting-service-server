import abc
from typing import Any
from uuid import UUID


class AbstractTaskRepository(abc.ABC):
    session: Any
