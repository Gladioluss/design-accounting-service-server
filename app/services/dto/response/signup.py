from uuid import UUID
from pydantic import BaseModel


class SignUpServiceResponseDTO(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
