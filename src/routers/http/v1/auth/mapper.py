from src.models.auth import AuthModel

from .schema import (
    SigninRequest,
    SigninResponse,
    SignupRequest,
)


class AuthRequestMapper:
    @staticmethod
    def create_singup_request_to_model(instance: SignupRequest) -> AuthModel:
        return AuthModel(
            first_name=instance.first_name,
            last_name=instance.last_name,
            middle_name=instance.middle_name,
            email=instance.email,
            password=instance.password
        )

    @staticmethod
    def create_singin_request_to_model(instance: SigninRequest) -> AuthModel:
        return AuthModel(
            email=instance.email,
            password=instance.password
        )

class AuthResponseMapper:
    @staticmethod
    def entity_to_response(instance: AuthModel, access_token: str) -> SigninResponse:
        return SigninResponse(
            id=instance.id,
            first_name=instance.first_name,
            last_name=instance.last_name,
            middle_name=instance.middle_name,
            email=instance.email,
            access_token=access_token
        )
