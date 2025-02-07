from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from src.errors.user import UserNotFoundError
from src.errors.token import TokenError
from src.errors.auth import (
    UserAlreadyExists
)


def add_exception_handlers(app: FastAPI):
    ### Auth errors ###
    @app.exception_handler(UserAlreadyExists)
    async def handle_user_already_exists_error(_, exc):
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            }, 
            status_code=status.HTTP_409_CONFLICT
        )
    

    @app.exception_handler(UserAlreadyExists)
    async def handle_user_validate_error(_, exc):
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            }, 
            status_code=status.HTTP_401_UNAUTHORIZED
        )
   
   
   ### Token errors ###
    @app.exception_handler(TokenError)
    async def handle_token_error(_, exc):
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            }, 
            status_code=status.HTTP_403_FORBIDDEN
        )
    
    ### User errors ###
    @app.exception_handler(UserNotFoundError)
    async def handle_user_not_found_error(_, exc):
        return JSONResponse(
            content={
                'error': f'{type(exc).__name__}: {exc}'
            }, 
            status_code=status.HTTP_404_NOT_FOUND
        )