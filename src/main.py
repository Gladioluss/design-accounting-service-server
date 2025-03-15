from fastapi import FastAPI
from src.configs.settings.settings import settings
from src.routers.http.v1.api import APIV1Router
from src.routers.http.v1.error_handler import add_exception_handlers
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.API_TITLE, prefix=settings.API_PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    router=APIV1Router, prefix=settings.API_PREFIX
)

add_exception_handlers(app=app)

@app.get("/health")
async def health():
    return 200
