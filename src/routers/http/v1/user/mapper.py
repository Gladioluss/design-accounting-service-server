
from src.models.user import UserModel
from .schema import GetAllUsersResponseModel


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