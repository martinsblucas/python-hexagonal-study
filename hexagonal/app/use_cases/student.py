from uuid import UUID

from app.adapters.outbound.repositories import StudentRepository
from app.domain.models import StudentIn, StudentOut


class StudentUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    async def all(self) -> list[StudentOut]:
        return await self.repository.all()

    async def find(self, student_id: UUID) -> StudentOut:
        return await self.repository.find(student_id=student_id)

    async def create(self, student: StudentIn) -> StudentOut:
        return await self.repository.create(student=student)

    async def update(self, student_id, student: StudentIn) -> StudentOut:
        return await self.repository.update(student_id=student_id, student=student)

    async def delete(self, student_id: UUID) -> None:
        return await self.repository.delete(student_id=student_id)
