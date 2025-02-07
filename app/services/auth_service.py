from fastapi import Depends
from app.models.auth import AuthModel
from app.repositories.user_repository import UserRepository
from app.services.dto.request.signup import SignUpServiceRequestDTO, signup_service_request_dto_to_auth_model
from app.services.dto.response.signup import SignUpServiceResponseDTO


class AuthService:
    userRepository: UserRepository

    def __init__(
        self, 
        userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    async def signup(
        self, 
        sign_up_service_response_dto: SignUpServiceRequestDTO
    ) -> SignUpServiceResponseDTO:
        user: AuthModel = signup_service_request_dto_to_auth_model(sign_up_service_response_dto)
        res = await self.userRepository.create_user(user)
        return