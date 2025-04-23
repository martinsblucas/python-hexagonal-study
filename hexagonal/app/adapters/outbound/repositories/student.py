from uuid import UUID

from app.adapters.outbound.orm.models import Student
from app.domain.exceptions import NotFound, PersistenceError
from app.domain.models import StudentIn, StudentOut
from app.domain.ports.repositories import AbstractStudentRepository
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class StudentRepository(AbstractStudentRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def all(self) -> list[StudentOut]:
        try:
            result = await self.session.scalars(
                select(Student).order_by(Student.created_at.desc())
            )

            return [StudentOut.model_validate(r) for r in result.all()]

        except SQLAlchemyError as error:
            raise PersistenceError() from error

    async def find(self, student_id: UUID) -> StudentOut:
        try:
            result = await self.session.execute(
                select(Student).where(Student.id == student_id)
            )

            return StudentOut.model_validate(result.scalars().one())

        except NoResultFound as error:
            raise NotFound() from error

        except SQLAlchemyError as error:
            raise PersistenceError() from error

    async def create(self, student: StudentIn) -> StudentOut:
        try:
            result = await self.session.execute(
                insert(Student).values(**student.model_dump()).returning(Student)
            )

            find_student = StudentOut.model_validate(result.scalars().one())
            await self.session.commit()
            return find_student

        except SQLAlchemyError as error:
            raise PersistenceError() from error

    async def update(self, student_id: UUID, student: StudentIn) -> StudentOut:
        try:
            result = await self.session.execute(
                update(Student)
                .where(Student.id == student_id)
                .values(**student.model_dump())
                .returning(Student)
            )

            find_student = StudentOut.model_validate(result.scalars().one())
            await self.session.commit()
            return find_student

        except NoResultFound as error:
            raise NotFound() from error

        except SQLAlchemyError as error:
            raise PersistenceError() from error

    async def delete(self, student_id: UUID) -> None:
        try:
            result = await self.session.execute(
                delete(Student).where(Student.id == student_id).returning(Student)
            )

            result.scalars().one()
            await self.session.commit()
            return None

        except NoResultFound as error:
            raise NotFound() from error

        except SQLAlchemyError as error:
            raise PersistenceError() from error
