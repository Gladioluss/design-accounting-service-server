from fastapi import APIRouter, Depends

from app.configs.settings.settings import settings
from app.routers.v1.dto.request.signup import SignUpRequestDTO, signup_request_dto_to_signup_service_request_dto
from app.routers.v1.dto.response.get_all_users import GetAllUsersPaginateResponseDTO, GetAllUsersPaginateResponseDTO, get_all_users_service_paginate_response_dto_to_get_all_users_paginate_response_dto
from app.routers.v1.dto.response.signup import SignUpResponseDTO, sign_up_service_response_dto_to_sign_up_response_dto
from app.services.user_service import UserService


UserRouter = APIRouter(
    prefix=f"{settings.API_PREFIX}/v1/user", tags=["user"]
)



# @UserRouter.get("/")
# async def _def_user_by_id():
#     ...


@UserRouter.get("/", response_model=GetAllUsersPaginateResponseDTO)
async def _get_all_users_paginate(
    pageSize: int | None = 100,
    startIndex: int | None = 0,
    user_service: UserService = Depends()
) -> GetAllUsersPaginateResponseDTO:
    result = await user_service.get_all_users(pageSize=pageSize, startIndex=startIndex)
    return get_all_users_service_paginate_response_dto_to_get_all_users_paginate_response_dto(result)
