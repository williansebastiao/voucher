from fastapi import FastAPI

from app.core.settings import settings
from app.routers.api import router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=f"{settings.APP_PATH}/docs",
    redoc_url=f"{settings.APP_PATH}/redoc",
    openapi_url=f"{settings.APP_PATH}/openapi.json",
)

app.include_router(router, prefix=settings.APP_PATH)
