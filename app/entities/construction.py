from uuid import UUID
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.dialects.postgresql import JSON

from app.utils.uuid import uuid7


class Construction(SQLModel, table=True):
    __tablename__ = "construction"

    id: UUID = Field(
        default_factory=uuid7,
        primary_key=True,
        index=True,
        nullable=False
    )
    barcode_number: int
    # properties: dict = Field(default=None, sa_column=JSON)
    
    tasks: list["Task"] = Relationship(
        back_populates="construction",
        sa_relationship_kwargs={"lazy": "selectin"}
    )