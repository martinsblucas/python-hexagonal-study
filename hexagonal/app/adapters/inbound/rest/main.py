from contextlib import asynccontextmanager

from app.adapters.inbound.rest.v1.students import router as students_router
from app.configs.dependency_injection import Container
from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI


@asynccontextmanager
@inject
async def lifespan(_: FastAPI, session_manager=Provide[Container.session_manager]):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    await session_manager.close()


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI(
        lifespan=lifespan, title="Hexagonal Architecture Practice", version="1.0.0"
    )

    app.container = container
    app.include_router(students_router)
    return app


app = create_app()
