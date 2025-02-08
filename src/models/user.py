from uuid import UUID
from pydantic import BaseModel


# class UserModel(BaseModel):
#     id: UUID
#     first_name: str
#     last_name: str
#     middle_name: str | None = None
#     email: str
#     password: str
#     updated_at TIMESTAMP,
#     created_at TIMESTAMP,
#     is_admin BOOLEAN,
#     is_verify BOOLEAN,
#     is_deleted BOOLEAN