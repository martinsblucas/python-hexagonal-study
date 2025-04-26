from typing import Annotated

from app.configs.dependency_injection import Container
from app.use_cases import StudentUseCase
from dependency_injector.wiring import Provide
from fastapi import Depends

StudentUseCaseDep = Annotated[
    StudentUseCase, Depends(Provide[Container.student_use_case])
]
