import abc
from typing import Any

from src.models.user import UserModel


class AbstractUserRepository(abc.ABC):
    session: Any

    @abc.abstractmethod
    async def get_all_users(self, limit: int, offset: int) -> tuple[list[UserModel], int]:
        raise NotImplementedError