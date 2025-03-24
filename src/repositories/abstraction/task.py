import abc
from typing import Any


class AbstractTaskRepository(abc.ABC):
    session: Any
