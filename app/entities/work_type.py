from uuid import UUID
from sqlmodel import Field, Relationship, SQLModel

from app.utils.uuid import uuid7


class WorkType(SQLModel, table=True):
    __tablename__ = "work_type"
    
    id: UUID = Field(
        default_factory=uuid7,
        primary_key=True,
        index=True,
        nullable=False
    )
    name: str
    
    tasks: list["Task"] = Relationship(
        back_populates="work_type",
        sa_relationship_kwargs={"lazy": "selectin"}
    )