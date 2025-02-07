

from fastapi import Depends
from app.models.user import UserModel
from app.repositories.user_repository import UserRepository
from app.services.dto.request.signup import SignUpServiceRequestDTO, signup_service_request_dto_to_auth_model
from app.services.dto.response.get_all_users import GetAllUsersServicePaginateResponseDTO, user_model_to_get_all_users_service_response_dto


class UserService:
    userRepository: UserRepository

    def __init__(
        self, 
        userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    async def get_all_users(
        self,
        pageSize: int | None = 100,
        startIndex: int | None = 0,
    ) -> GetAllUsersServicePaginateResponseDTO:
        users: list[UserModel] = await self.userRepository.get_all_users(limit=pageSize, start=startIndex)
        
        total_count: int = await self.userRepository.get_total_count()

        total_pages: int = (total_count + pageSize - 1) // pageSize
        current_page: int = (startIndex // pageSize) + 1

        return GetAllUsersServicePaginateResponseDTO(
            total_count=total_count,
            page_size=pageSize,
            current_page=current_page,
            total_pages=total_pages,
            items=[user_model_to_get_all_users_service_response_dto(user) for user in users]
        )

    async def create_user(self, sign_up_service_response_dto: SignUpServiceRequestDTO) -> UserModel:
        user: UserModel = signup_service_request_dto_to_auth_model(sign_up_service_response_dto)
        return await self.userRepository.create_user(user)

    async def get_user_by_id(self,):
        return self.userRepository.get_user_by_id()