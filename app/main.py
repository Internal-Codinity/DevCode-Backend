from fastapi import FastAPI

from .api.v1.router import api_router
from .core.startup import configure_app

app = FastAPI(
    title="Codex Backend",
    description="Codex backend API",
    version="1.0.0"
)

configure_app(app)

@app.get("/")
async def root():
    return {"status": "ok", "service": "Codex Backend"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(
    api_router,
    prefix="/api/v1"
)



# app setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests
# 