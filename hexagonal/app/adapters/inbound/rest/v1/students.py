from uuid import UUID

from app.adapters.inbound.rest.dependencies.core import StudentRepositoryDep
from app.adapters.inbound.rest.v1.models import (
    StudentV1Request,
    StudentV1Response,
)
from app.domain.exceptions import NotFound, PersistenceError
from app.domain.models import StudentIn
from dependency_injector.wiring import inject
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/v1/students", tags=["students"])


@router.get("/", response_model=list[StudentV1Response])
@inject
async def all(student_repository: StudentRepositoryDep):
    students = await student_repository.all()
    try:
        return [StudentV1Response.model_validate(student) for student in students]

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/{student_id}", response_model=StudentV1Response)
@inject
async def find(
    student_id: UUID,
    student_repository: StudentRepositoryDep,
):
    try:
        student = await student_repository.find(student_id=student_id)
        return StudentV1Response.model_validate(student)

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.post("/", response_model=StudentV1Response)
@inject
async def create(
    student_repository: StudentRepositoryDep, student_request: StudentV1Request
):
    try:
        student = await student_repository.create(
            student=StudentIn.model_validate(student_request)
        )

        return StudentV1Response.model_validate(student)

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.put("/{student_id}", response_model=StudentV1Response)
@inject
async def update(
    student_id: UUID,
    student_repository: StudentRepositoryDep,
    student_request: StudentV1Request,
):
    try:
        student = await student_repository.update(
            student_id=student_id, student=StudentIn.model_validate(student_request)
        )

        return StudentV1Response.model_validate(student)

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.delete(
    "/{student_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
@inject
async def delete(
    student_id: UUID,
    student_repository: StudentRepositoryDep,
):
    try:
        await student_repository.delete(student_id=student_id)
        return None

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
