import abc
from typing import Any
from uuid import UUID


class AbstractStageCheckRepository(abc.ABC):
    session: Any
