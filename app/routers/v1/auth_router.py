from fastapi import APIRouter, Depends

from app.configs.settings.settings import settings
from app.configs.security.jwt import AuthJWT
from app.routers.v1.dto.request.signup import (
    SignUpRequestDTO, 
    signup_request_dto_to_signup_service_request_dto
)
from app.routers.v1.dto.response.signup import SignUpResponseDTO, sign_up_service_response_dto_to_sign_up_response_dto
from app.services.auth_service import AuthService

ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN


AuthRouter = APIRouter(
    prefix=f"{settings.API_PREFIX}/v1/user", tags=["user"]
)


@AuthRouter.post("/signup")
async def _signup(
    signup_request_dto: SignUpRequestDTO,
    auth_service: AuthService = Depends()
) -> SignUpResponseDTO:
    signup_service_request_dto = signup_request_dto_to_signup_service_request_dto(signup_request_dto)
    result = await auth_service.signup(sign_up_service_response_dto=signup_service_request_dto)
    return sign_up_service_response_dto_to_sign_up_response_dto(sign_up_service_response_dto=result)


@AuthRouter.post("/signin")
async def _signin(
    authorize: AuthJWT = Depends(),
    auth_service: AuthService = Depends()
):
    raise NotImplementedError


@AuthRouter.post("/change_password")
async def _change_password():
    raise NotImplementedError


@AuthRouter.get("/refresh")
async def _refresh():
    raise NotImplementedError


@AuthRouter.get("/logout")
async def _logout():
    raise NotImplementedError