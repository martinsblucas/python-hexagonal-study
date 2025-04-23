"""The interface for the student repository"""

from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models import StudentIn, StudentOut


class AbstractStudentRepository(ABC):
    """The abstract class for the student repository"""

    @abstractmethod
    async def all(self) -> list[StudentOut]:
        """List all students

        :raises PersistenceError: if an unexpected error occurs during the operation
        :return: A list of students
        :rtype: list[StudentOut]
        """

    @abstractmethod
    async def find(self, student_id: UUID) -> StudentOut:
        """Find a student by id

        :param student_id: The id of the student
        :type student_id: UUID
        :raises NotFound: if the student is not found
        :raises PersistenceError: if an unexpected error occurs during the operation
        :return: The student
        :rtype: StudentOut
        """

    @abstractmethod
    async def create(self, student: StudentIn) -> StudentOut:
        """Create a new student

        :param student: The student to create
        :type student: StudentIn
        :raises PersistenceError: if an unexpected error occurs during the operation
        :return: The created student
        :rtype: StudentOut
        """

    @abstractmethod
    async def update(self, student_id: UUID, student: StudentIn) -> StudentOut:
        """Update a student

        :param student_id: The id of the student
        :type student_id: UUID
        :param student: The student to update
        :type student: StudentIn
        :raises NotFound: if the student is not found
        :raises PersistenceError: if an unexpected error occurs during the operation
        :return: The updated student
        :rtype: StudentOut
        """

    @abstractmethod
    async def delete(self, student_id: UUID) -> None:
        """Delete a student

        :param student_id: The id of the student to delete
        :type student_id: UUID
        :raises NotFound: if the student is not found
        :raises PersistenceError: if an unexpected error occurs during the operation
        """
