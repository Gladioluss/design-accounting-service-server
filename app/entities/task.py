from uuid import UUID
from sqlmodel import Field, Relationship, SQLModel

from app.entities.construction import Construction
from app.entities.user import User
from app.entities.work_type import WorkType
from app.utils.uuid import uuid7


class Task(SQLModel, table=True):
    __tablename__ = "task"

    id: UUID = Field(
        default_factory=uuid7,
        primary_key=True,
        index=True,
        nullable=False
    )    
    construction_id: UUID | None = Field(foreign_key="construction.id")
    user_id: UUID | None = Field(foreign_key="user.id")
    work_type_id: UUID | None = Field(foreign_key="work_type.id")
    
    construction: Construction | None = Relationship(
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "Task.construction_id==Construction.id",
        }
    )

    user: User | None = Relationship(
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "Task.user_id==User.id",
        }
    )

    work_type: WorkType | None = Relationship(
        sa_relationship_kwargs={
            "lazy": "joined",
            "primaryjoin": "Task.work_type_id==WorkType.id",
        }
    )
