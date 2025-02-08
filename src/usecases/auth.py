from fastapi import BackgroundTasks, Response

from src.models.refresh_token import RefreshTokenModel
from src.configs.settings.settings import settings
from src.errors.auth import UserAlreadyExists, UserNotFoundError
from src.configs.security.security import create_access_token, create_refresh_token, encrypt_password
from src.models.auth import AuthModel
from src.di.unit_of_work import AbstractUnitOfWork
from src.utils.authenticate import authenticate
from src.utils.verification.send_verification_mail import send_verification_mail
from src.utils.verification.generate_verify_token import generate_verification_token


async def signup(
   async_unit_of_work: AbstractUnitOfWork, 
   data: AuthModel,
   background_tasks: BackgroundTasks
) -> None:
    async with async_unit_of_work as auow:
        user = await auow.auth_repo.get_by_email(email=data.email)

        if user:
            raise UserAlreadyExists(data.email)
        
        data.password = encrypt_password(password=data.password)
        await auow.auth_repo.create(data=data)
        
        user_verify_token = await auow.auth_repo.get_verify_token_by_user_email(email=data.email)

    background_tasks.add_task(
        send_verification_mail, 
        data.email, 
        user_verify_token
    )

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
    
    async with async_unit_of_work as auow:
        await auow.refresh_token_repo.create(
            data=RefreshTokenModel(
                user_id=user.id,
                refresh_token=refresh_token
            )
        )

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

async def verify_email(
    async_unit_of_work: AbstractUnitOfWork, 
    email: str,
    verify_token: str
):
    async with async_unit_of_work as auow:     
        user_verify_token = await auow.auth_repo.get_verify_token_by_user_email(email=email)

        if user_verify_token is None:
            raise UserNotFoundError(email)

        if user_verify_token != verify_token:
            raise
        await auow.auth_repo.verify_user_by_user_email(email=email)


async def verify_email_new(
    async_unit_of_work: AbstractUnitOfWork, 
    email: str,
    background_tasks: BackgroundTasks,
):
    verify_token = generate_verification_token()

    async with async_unit_of_work as auow:
        user_verify_token = await auow.auth_repo.update_verify_token_by_user_email(email=email, verify_token=verify_token)

        if user_verify_token is None:
            raise UserNotFoundError(email)
        
    background_tasks.add_task(
        send_verification_mail, 
        email, 
        user_verify_token
    )