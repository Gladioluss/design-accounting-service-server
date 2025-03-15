from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class UserResponseModel(BaseModel):
    id: UUID | None = None
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    updated_at: datetime | None = None
    created_at: datetime | None = None


class GetAllUsersResponseModel(BaseModel):
    page: int = 0
    size: int = 50
    next_count: int
    users: list[UserResponseModel]

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str