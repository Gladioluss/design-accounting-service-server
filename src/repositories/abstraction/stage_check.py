import abc
from typing import Any


class AbstractStageCheckRepository(abc.ABC):
    session: Any
