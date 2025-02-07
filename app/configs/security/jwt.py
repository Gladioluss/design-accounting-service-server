import base64
from typing import List
from fastapi import Depends, HTTPException, status
from app.configs.settings.settings import settings
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from app import crud

class Settings(BaseModel):
    authjwt_algorithm: str = settings.JWT_ALGORITHM
    authjwt_decode_algorithms: List[str] = [settings.JWT_ALGORITHM]
    authjwt_token_location: set = {'cookies', 'headers'}
    authjwt_access_cookie_key: str = 'access_token'
    authjwt_refresh_cookie_key: str = 'refresh_token'
    authjwt_cookie_csrf_protect: bool = False
    authjwt_public_key: str = base64.b64decode(
        settings.JWT_PUBLIC_KEY
    ).decode('utf-8')
    authjwt_private_key: str = base64.b64decode(
        settings.JWT_PRIVATE_KEY
    ).decode('utf-8')


@AuthJWT.load_config
def get_config():
    return Settings()


def require_user(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
        user_id = authorize.get_jwt_subject()
        user = crud.user.get(user_id)

        if not user:
            raise IdUserNotFoundException(id=user_id)

    except Exception as e:
        error = e.__class__.__name__
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not logged in')
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exist')
        if error == 'NotVerified':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Please verify your account')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid or has expired')

    return user_id
