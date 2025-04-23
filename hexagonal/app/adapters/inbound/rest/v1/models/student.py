"""The models for the student entity"""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentV1Response(BaseModel):
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


class StudentV1Request(BaseModel):
    """The model for creating a student"""

    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    email: EmailStr = Field(max_length=100)
    date_of_birth: date
    cpf: str = Field(max_length=11)
