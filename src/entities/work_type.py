from datetime import datetime

from sqlalchemy import Column, DateTime, String, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

WorkType = table(
    "work_type",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("name", String(255)),
    Column("updated_at", DateTime, default=datetime.now),
    Column("created_at", DateTime, default=datetime.now)
)
