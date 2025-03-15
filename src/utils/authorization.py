from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.configs.security import security
from src.errors.token import BadCredentials

get_bearer_token = HTTPBearer(auto_error=False)

async def authorization(
        auth: HTTPAuthorizationCredentials | None = Depends(get_bearer_token) # noqa: B008
) -> None:
    if not auth or not auth.credentials:
        raise BadCredentials()

    access_token_decoded = security.decode_token(token=auth.credentials)

    if access_token_decoded.get("type") != security.TokenType.access_token:
        raise BadCredentials()
    return access_token_decoded
