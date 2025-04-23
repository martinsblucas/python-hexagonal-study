from datetime import date

from app.adapters.outbound.orm.models import BaseModel
from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column


class Student(BaseModel):
    """The student model"""

    __tablename__ = "students"

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date(), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
