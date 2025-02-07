from fastapi import FastAPI
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.configs.settings.settings import settings
from app.routers.v1.user_router import UserRouter

def start_app() -> FastAPI:
    app = FastAPI(title=settings.API_TITLE, prefix=settings.API_PREFIX)

    app.include_router(UserRouter)

    if settings.CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    return app

app = start_app()