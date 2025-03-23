from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.configs.logging.logging import get_logger
from src.errors.auth import IncorrectLoginError, UserAlreadyExists
from src.errors.auth import UserNotFoundError as UserNotFoundErrorAuth
from src.errors.token import (
    BadCredentials,
    TokenDecodeError,
    TokenError,
    TokenExpiredSignatureError,
    TokenMissingRequiredClaimError,
    WrongVerifyToken,
)
from src.errors.user import UserNotFoundError as UserNotFoundErrorUser
from src.errors.work_type import WorkTypeAlreadyExists
from starlette import status

logger = get_logger("Error handler")

def add_exception_handlers(app: FastAPI):

    ## Auth errors ###
    @app.exception_handler(UserAlreadyExists)
    async def handle_user_already_exists_error(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            },
            status_code=status.HTTP_409_CONFLICT
        )


    @app.exception_handler(UserNotFoundErrorAuth)
    async def handle_user_not_found_error_auth(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            },
            status_code=status.HTTP_404_NOT_FOUND
        )


    @app.exception_handler(IncorrectLoginError)
    async def handle_incorrect_login_error(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc.message}'
            },
            status_code=status.HTTP_401_UNAUTHORIZED
        )

   ### Token errors ###
    @app.exception_handler(TokenError)
    @app.exception_handler(TokenExpiredSignatureError)
    @app.exception_handler(TokenDecodeError)
    @app.exception_handler(TokenMissingRequiredClaimError)
    @app.exception_handler(WrongVerifyToken)
    @app.exception_handler(BadCredentials)
    async def handle_token_error(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            },
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    ### User errors ###
    @app.exception_handler(UserNotFoundErrorUser)
    async def handle_user_not_found_error_user(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            },
            status_code=status.HTTP_404_NOT_FOUND
        )

    ### Work type errors ###
    @app.exception_handler(WorkTypeAlreadyExists)
    async def handle_work_type_already_exists_error(_, exc):
        logger.error(f'{type(exc).__name__}: {exc}')
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            },
            status_code=status.HTTP_409_CONFLICT
        )
