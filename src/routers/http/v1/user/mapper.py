
from src.models.user import UserModel

from .schema import CreateUserRequest, GetAllUsersResponseModel, UserResponseModel


class UserRequestMapper:
    @staticmethod
    def create_user_request_to_model(instance: CreateUserRequest) -> UserModel:
        return UserModel(
            first_name=instance.first_name,
            last_name=instance.last_name,
            middle_name=instance.middle_name,
            email=instance.email,
            password=instance.password
        )


class UserResponseMapper:
    
    @staticmethod
    def get_all_users_to_response(
        instance: list[UserModel], 
        page: int, 
        size: int, 
        next_count: int
    ) -> GetAllUsersResponseModel:
        return GetAllUsersResponseModel(
            page=page,
            size=size,
            next_count=next_count,
            users=[
                UserResponseModel(
                    id=e.id,
                    first_name=e.first_name,
                    last_name=e.last_name,
                    middle_name=e.middle_name,
                    email=e.email,
                    updated_at=e.updated_at,
                    created_at=e.created_at,
                ) for e in instance
            ]
        )
    
    @staticmethod
    def user_to_response(
        instance: UserModel,
    ) -> UserResponseModel:
        return UserResponseModel(
            id=instance.id,
            first_name=instance.first_name,
            last_name=instance.last_name,
            middle_name=instance.middle_name,
            email=instance.email,
            updated_at=instance.updated_at,
            created_at=instance.created_at,
        )
