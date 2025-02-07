from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.configs.settings.settings import settings
from src.di.unit_of_work import AbstractUnitOfWork
from src.di.dependency_injection import injector
from src.routers.http.v1.auth.mapper import AuthRequestMapper
from src.routers.http.v1.auth.schema import SignupRequest
from src.usecases import auth as auth_ucase

AuthRouter = APIRouter(prefix="/v1/auth", tags=["Auth"])

@AuthRouter.post("/signup", status_code=status.HTTP_201_CREATED)
async def _signup(
    body: SignupRequest
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    signup_data = AuthRequestMapper.create_request_to_model(body)
    await auth_ucase.signup(async_unit_of_work, signup_data)

@AuthRouter.post("/signin")
async def _signin(
    # authorize: AuthJWT = Depends(),
):
    raise NotImplementedError


@AuthRouter.post("/change_password")
async def _change_password():
    raise NotImplementedError


@AuthRouter.get("/refresh")
async def _refresh(
    
):
    raise NotImplementedError


@AuthRouter.get("/logout")
async def _logout(
):
    raise NotImplementedError