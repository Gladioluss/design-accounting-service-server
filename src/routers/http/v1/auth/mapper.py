from src.models.auth import (
    AuthModel
)

from .schema import (
    SignupRequest,
)

class AuthRequestMapper:
    @staticmethod
    def create_request_to_model(instance: SignupRequest) -> AuthModel:
        return AuthModel(
            first_name=instance.first_name,
            last_name=instance.last_name,
            middle_name=instance.middle_name,
            email=instance.email,
            password=instance.password
        )