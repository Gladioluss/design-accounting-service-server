from uuid import UUID
from pydantic import BaseModel

from app.entities.user import User


class AuthModel(BaseModel):
    id: UUID | None = None
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str

    class Config:
        orm_mode = True

def user_entity_to_model(user: User) -> UserModel:
    return UserModel(**user.model_dump())  