from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routers.http.v1.error_handler import add_exception_handlers
from src.configs.settings.settings import settings
from src.routers.http.v1.auth.router import AuthRouter
from src.routers.http.v1.user.router import UserRouter


app = FastAPI(title=settings.API_TITLE, prefix=settings.API_PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router=AuthRouter, prefix=settings.API_PREFIX)
app.include_router(router=UserRouter, prefix=settings.API_PREFIX)

add_exception_handlers(app=app)
