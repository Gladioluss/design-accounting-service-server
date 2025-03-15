from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, table
from sqlalchemy.dialects.postgresql import UUID
from src.utils.uuid import uuid7

CheckMeasurement = table(
    "check_measurement",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("stage_check_id", UUID(as_uuid=True), ForeignKey("stage_check.id")),
    Column("field_name", String(255)),
    Column("field_value", String(255)),
    Column("created_at", DateTime, default=datetime.now)
)
