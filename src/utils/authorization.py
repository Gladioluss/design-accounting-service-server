from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.configs.security import security

get_bearer_token = HTTPBearer(auto_error=False)

async def authorization(
        auth: HTTPAuthorizationCredentials | None = Depends(get_bearer_token) # noqa: B008
) -> None:

    access_token_decoded = security.decode_token(
        token=authorization.access_token)
    if access_token_decoded["type"] != security.TokenType.access_token:
        # raise TokenIncorrectException()
        raise
    return authorization
