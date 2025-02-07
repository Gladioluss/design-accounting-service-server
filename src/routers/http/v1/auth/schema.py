from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str