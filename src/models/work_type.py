from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class WorkTypeModel(BaseModel):
    id: UUID | None = None
    name: str
    updated_at: datetime | None = None
    created_at: datetime | None = None
