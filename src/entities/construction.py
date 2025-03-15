from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Integer, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

Construction = table(
    "construction",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("barcode_number", Integer),
    Column("properties", JSON),
    Column("updated_at", DateTime, default=datetime.now),
    Column("created_at", DateTime, default=datetime.now)
)
