from uuid import UUID
from pydantic import BaseModel


class AuthModel(BaseModel):
    id: UUID | None = None
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str