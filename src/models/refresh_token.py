from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class RefreshTokenModel(BaseModel):
    id: UUID | None = None
    user_id: UUID
    refresh_token: str