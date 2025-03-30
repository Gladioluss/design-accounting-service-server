from fastapi import FastAPI, Request
from src.configs.logging.logging import get_logger, get_logger_options
from src.configs.settings.settings import settings
from src.routers.http.v1.api import APIV1Router
from src.routers.http.v1.error_handler import add_exception_handlers
from starlette.middleware.cors import CORSMiddleware

logger = get_logger(settings.API_TITLE)
logger.info("Starting application")


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


@app.middleware("http")
async def log_requests(req: Request, call_next):
    from src.utils.uuid import uuid7
    req.state.req_id = uuid7()

    opts = get_logger_options(settings.API_TITLE,req)
    logger = opts["logger"]
    custom_req_props = opts["custom_props"]
    custom_req_props.update({"method": req.method})
    custom_req_props.update({"url": req.url.path})
    custom_req_props.update({"query": dict(req.query_params)})
    custom_req_props.update({"params": dict(req.path_params)})
    custom_req_props.update({"headers": dict(req.headers)})
    logger.info("Incoming request", extra=custom_req_props)
    response = await call_next(req)

    custom_res_props = opts["custom_props"]
    custom_res_props.update({"status_code": response.status_code})
    logger.info("Request completed", extra=custom_res_props)
    return response


@app.get("/health")
async def health():
    return 200
