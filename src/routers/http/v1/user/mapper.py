
from src.models.user import UserModel
from .schema import GetAllUsersResponseModel, UserResponseModel


class UserResponseMapper:
    
    @staticmethod
    def get_all_users_to_response(
        instance: UserModel, 
        page: int, 
        size: int, 
        next_count: int
    ) -> GetAllUsersResponseModel:
        return GetAllUsersResponseModel(
            page=page,
            size=size,
            next_count=next_count,
            users=instance
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