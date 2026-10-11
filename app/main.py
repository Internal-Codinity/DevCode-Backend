from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api.v1.router import api_router
from .core.startup import configure_app
from app.core.logger import setup_logging
from app.core.startup import initialize_resources

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform startup tasks here
    await initialize_resources()
    yield
    # Add resource cleanup here when needed.
    await configure_app(app)
    yield
    # Perform shutdown tasks here

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Learning FastAPI backend",
    lifespan=lifespan,
)

configure_app(app)

@app.get("/", tags=["Root"])
async def root():
    return {"status": "ok", "service": "Codex Backend"}

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

app.include_router(
    api_router,
    prefix="/api/v1",
    tags=["API"]
)



# app setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests
# 