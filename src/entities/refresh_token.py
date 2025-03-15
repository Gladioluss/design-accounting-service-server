from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

RefreshToken = table(
    "refresh_token",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("refresh_token", String(255)),
    Column("created_at", DateTime, default=datetime.now),
)
