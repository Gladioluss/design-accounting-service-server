from pydantic import BaseModel
from src.models.user import UserModel

class GetAllUsersResponseModel(BaseModel):
    page: int = 0
    size: int = 50
    next_count: int
    users: list[UserModel]
