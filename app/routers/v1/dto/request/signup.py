from pydantic import BaseModel

from app.services.dto.request.signup import SignUpServiceRequestDTO


class SignUpRequestDTO(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    password: str

def signup_request_dto_to_signup_service_request_dto(
    sign_up_request_dto: SignUpRequestDTO
) -> SignUpServiceRequestDTO:
    return SignUpServiceRequestDTO(
        first_name=sign_up_request_dto.first_name,
        last_name=sign_up_request_dto.first_name,
        middle_name=sign_up_request_dto.first_name,
        email=sign_up_request_dto.first_name,
        password=sign_up_request_dto.first_name,
    )