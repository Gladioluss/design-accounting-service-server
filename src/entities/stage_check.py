from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

StageCheck = table(
    "stage_check",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("check_name", String(255)),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("created_at", DateTime, default=datetime.now)
)
