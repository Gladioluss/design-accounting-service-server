from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

Defect = table(
    "defect",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("barcode_id", UUID(as_uuid=True), ForeignKey("construction.id")),
    Column("defect_type", String(255)),
    Column("description", Text),
    Column("photo", String(255)),
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("scan_time", DateTime, default=datetime.now)
)
