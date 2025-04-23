from typing import Annotated

from app.adapters.outbound.repositories import StudentRepository
from app.configs.dependency_injection import Container
from dependency_injector.wiring import Provide
from fastapi import Depends

StudentRepositoryDep = Annotated[
    StudentRepository, Depends(Provide[Container.student_repository])
]
