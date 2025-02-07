from uuid import UUID
from pydantic import BaseModel


class AuthModel(BaseModel):
    id: UUID | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    email: str
    password: str