from uuid import UUID
from pydantic import BaseModel

from app.services.dto.response.get_all_users import GetAllUsersServicePaginateResponseDTO

class GetAllUsersResponseDTO(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    email: str

class GetAllUsersPaginateResponseDTO(BaseModel):
    total_count: int
    page_size: int
    current_page: int
    total_pages: int
    items: list[GetAllUsersResponseDTO]

def get_all_users_service_paginate_response_dto_to_get_all_users_paginate_response_dto(
    users_service_dto: GetAllUsersServicePaginateResponseDTO
)-> GetAllUsersPaginateResponseDTO:
    return GetAllUsersPaginateResponseDTO(
            total_count=users_service_dto.total_count,
            page_size=users_service_dto.page_size,
            current_page=users_service_dto.current_page,
            total_pages=users_service_dto.total_pages,
            items=[
                GetAllUsersResponseDTO(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    middle_name=user.middle_name,
                    email=user.email
                )
                for user in users_service_dto.items
            ]
        )
