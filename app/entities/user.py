from uuid import UUID
from sqlalchemy import Boolean, Column, String
from sqlmodel import Field, Relationship, SQLModel
from app.utils.uuid import uuid7


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: UUID = Field(
        default_factory=uuid7,
        primary_key=True,
        index=True,
        nullable=False
    )
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str = Field(
        sa_column=Column(
            String,
            unique=True,
            nullable=False
        )
    )
    password: str = Field(sa_column=Column(String, nullable=False))
    is_admin: bool = False
    is_verify: bool = False
    is_deleted: bool = False

    tasks: list["Task"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"lazy": "selectin"}
    )