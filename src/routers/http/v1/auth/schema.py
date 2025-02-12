from uuid import UUID

from pydantic import BaseModel


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str


class SigninRequest(BaseModel):
    email: str
    password: str


class SigninResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    access_token: str
