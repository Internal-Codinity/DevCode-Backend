from fastapi import FastAPI

from .logger import logger


def on_startup() -> None:
    logger.info("Starting Codex application")


def on_shutdown() -> None:
    logger.info("Stopping Codex application")


def configure_app(app: FastAPI) -> None:
    app.on_event("startup")(on_startup)
    app.on_event("shutdown")(on_shutdown)



# app startup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests 