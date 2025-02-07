from fastapi import APIRouter, Depends, Response, status

from src.di.unit_of_work import AbstractUnitOfWork
from src.di.dependency_injection import injector
from src.routers.http.v1.auth.mapper import AuthRequestMapper, AuthResponseMapper
from src.routers.http.v1.auth.schema import SigninRequest, SignupRequest
from src.usecases import auth as auth_ucase
from src.utils.authorization import authorization


AuthRouter = APIRouter(prefix="/v1/auth", tags=["Auth"])

@AuthRouter.post("/signup", status_code=status.HTTP_201_CREATED)
async def _signup(
    body: SignupRequest
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    signup_data = AuthRequestMapper.create_singup_request_to_model(body)
    await auth_ucase.signup(
        async_unit_of_work=async_unit_of_work, 
        data=signup_data
    )

@AuthRouter.post("/signin")
async def _signin(
    response: Response,
    body: SigninRequest
):
    async_unit_of_work = injector.get(AbstractUnitOfWork)
    
    signup_data = AuthRequestMapper.create_singin_request_to_model(body)
    
    user, access_token = await auth_ucase.signin(
        async_unit_of_work=async_unit_of_work, 
        response=response,
        data=signup_data
    )

    return AuthResponseMapper.entity_to_response(
        instance=user,
        access_token=access_token
    )

@AuthRouter.post("/change_password")
async def _change_password(
    token: str = Depends(authorization)
):
    raise NotImplementedError


@AuthRouter.get("/refresh")
async def _refresh(
    
):
    raise NotImplementedError


@AuthRouter.get("/logout")
async def _logout(
):
    raise NotImplementedError