from datetime import timedelta
from fastapi import Response
from src.configs.settings.settings import settings
from src.errors.auth import UserAlreadyExists
from src.configs.security.security import create_access_token, create_refresh_token, encrypt_password
from src.models.auth import AuthModel
from src.di.unit_of_work import AbstractUnitOfWork
from src.utils.authenticate import authenticate


async def signup(
   async_unit_of_work: AbstractUnitOfWork, 
   data: AuthModel     
) -> None:
    async with async_unit_of_work as auow:
        user = await auow.auth_repo.get_by_email(email=data.email)

        if user is not None:
            raise UserAlreadyExists(data.email)
        data.password = encrypt_password(password=data.password)
        await auow.auth_repo.create(data=data)

async def signin(
    async_unit_of_work: AbstractUnitOfWork, 
    response: Response,
    data: AuthModel   
) -> tuple[AuthModel, str]:
    user = await authenticate(async_unit_of_work=async_unit_of_work, data=data)
    
    access_token = create_access_token(
        subject=str(user.id))

    refresh_token = create_refresh_token(
        subject=str(user.id))

    response.set_cookie(
        key='refresh_token', 
        value=refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRES_IN, 
        expires=settings.REFRESH_TOKEN_EXPIRES_IN, 
        path='/', 
        domain=None, 
        secure=True, 
        httponly=True, 
        samesite='lax'
    )
    return user, access_token
