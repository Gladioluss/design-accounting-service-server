from src.models.work_type import WorkTypeModel

from .schema import CreateWorkTypeRequest


class WorkTypeRequestMapper:
    @staticmethod
    def create_work_type_request_to_model(instance: CreateWorkTypeRequest) -> WorkTypeModel:
        return WorkTypeModel(
            name=instance.name,
        )
