from pydantic import BaseModel

from app.models.auth import AuthModel


class SignUpServiceRequestDTO(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    password: str


def signup_service_request_dto_to_auth_model(
    signup_service_request_dto: SignUpServiceRequestDTO
) -> AuthModel:
    return AuthModel(
        first_name=signup_service_request_dto.first_name,
        last_name=signup_service_request_dto.last_name,
        middle_name=signup_service_request_dto.middle_name,
        email=signup_service_request_dto.email,
        password=signup_service_request_dto.password
    )