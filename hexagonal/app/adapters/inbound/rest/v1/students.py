from uuid import UUID

from app.adapters.inbound.rest.dependencies.core import StudentUseCaseDep
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
async def all(student_use_case: StudentUseCaseDep):
    students = await student_use_case.all()
    try:
        return [StudentV1Response.model_validate(student) for student in students]

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.get("/{student_id}", response_model=StudentV1Response)
@inject
async def find(
    student_id: UUID,
    student_use_case: StudentUseCaseDep,
):
    try:
        student = await student_use_case.find(student_id=student_id)
        return StudentV1Response.model_validate(student)

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error


@router.post("/", response_model=StudentV1Response)
@inject
async def create(
    student_use_case: StudentUseCaseDep, student_request: StudentV1Request
):
    try:
        student = await student_use_case.create(
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
    student_use_case: StudentUseCaseDep,
    student_request: StudentV1Request,
):
    try:
        student = await student_use_case.update(
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
    student_use_case: StudentUseCaseDep,
):
    try:
        await student_use_case.delete(student_id=student_id)
        return None

    except NotFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    except PersistenceError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
