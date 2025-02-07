from uuid import UUID
from pydantic import BaseModel


class SignUpResponseDTO(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    email: str

def sign_up_service_response_dto_to_sign_up_response_dto(sign_up_service_response_dto) -> SignUpResponseDTO:
    return SignUpResponseDTO(
        first_name=sign_up_service_response_dto.first_name,
        last_name=sign_up_service_response_dto.first_name,
        middle_name=sign_up_service_response_dto.first_name,
        email=sign_up_service_response_dto.first_name
    )