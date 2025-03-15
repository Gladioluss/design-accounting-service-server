from pydantic import BaseModel


class CreateWorkTypeRequest(BaseModel):
    name: str
