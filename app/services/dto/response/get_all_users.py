from uuid import UUID
from pydantic import BaseModel

from app.models.user import UserModel

class GetAllUsersServiceResponseDTO(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
    
class GetAllUsersServicePaginateResponseDTO(BaseModel):
    total_count: int
    page_size: int
    current_page: int
    total_pages: int
    items: list[GetAllUsersServiceResponseDTO] 

def user_model_to_get_all_users_service_response_dto(user: UserModel) -> GetAllUsersServiceResponseDTO:
    return GetAllUsersServiceResponseDTO(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        email=user.email
    )