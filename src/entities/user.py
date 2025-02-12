from sqlalchemy import Boolean, Column, DateTime, String, table
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from src.utils.uuid import uuid7


User = table(
    "user",
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid7),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("middle_name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("verify_token", String(255)),
    Column("updated_at", DateTime, default=datetime.now()),
    Column("created_at", DateTime, default=datetime.now()),
    Column("is_admin", Boolean),
    Column("is_verify", Boolean),
    Column("is_deleted", Boolean)
)