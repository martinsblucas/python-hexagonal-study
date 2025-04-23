"""The models for the student entity"""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class StudentIn(BaseModel):
    """The model for creating a student"""

    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    cpf: str


class StudentOut(BaseModel):
    """The model for reading a student"""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    cpf: str
    created_at: datetime
    updated_at: datetime
