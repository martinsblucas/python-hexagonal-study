from app.adapters.outbound.orm.session_manager import SessionManager, get_db_session
from app.adapters.outbound.repositories import StudentRepository
from app.configs.settings import settings
from app.use_cases import StudentUseCase
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Resource, Singleton


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            "app.adapters.inbound.rest.main",
            "app.adapters.inbound.rest.v1.students",
        ]
    )

    config = Configuration()
    config.from_pydantic(settings)
    session_manager = Singleton(
        SessionManager, host=config.DB_DSN(), engine_kwargs={"echo": config.DB_ECHO()}
    )

    db_session = Resource(get_db_session, session_manager=session_manager)
    student_repository = Factory(StudentRepository, session=db_session)
    student_use_case = Factory(StudentUseCase, repository=student_repository)
