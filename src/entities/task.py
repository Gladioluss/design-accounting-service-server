from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

Task = table(
    "task",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("is_done", Boolean),
    Column("construction_id", UUID(as_uuid=True), ForeignKey("construction.id")),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("work_type_id", UUID(as_uuid=True), ForeignKey("work_type.id")),
    Column("updated_at", DateTime, default=datetime.now),
    Column("created_at", DateTime, default=datetime.now)
)
