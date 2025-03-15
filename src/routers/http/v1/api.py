from fastapi import APIRouter

from .auth.router import AuthRouter
from .check_measurement.router import CheckMeasurement
from .construction.router import ConstructionRouter
from .defect.router import DefectRouter
from .stage_check.router import StageCheckRouter
from .task.router import TaskRouter
from .user.router import UserRouter
from .work_type.router import WorkTypeRouter

APIV1Router = APIRouter(prefix="/v1")

APIV1Router.include_router(
    router=AuthRouter,
)
APIV1Router.include_router(
    router=UserRouter,
)
APIV1Router.include_router(
    router=ConstructionRouter,
)
APIV1Router.include_router(
    router=TaskRouter,
)
APIV1Router.include_router(
    router=WorkTypeRouter,
)
APIV1Router.include_router(
    router=DefectRouter,
)
APIV1Router.include_router(
    router=StageCheckRouter,
)
APIV1Router.include_router(
    router=CheckMeasurement,
)
