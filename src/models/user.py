

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserModel(BaseModel):
    id: UUID | None = None
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str
    updated_at: datetime | None = None
    created_at: datetime | None = None
    is_admin: bool | None = None
    is_verify: bool | None = None
    is_deleted: bool | None = None


class UpdateUserModel(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    email: str | None = None
