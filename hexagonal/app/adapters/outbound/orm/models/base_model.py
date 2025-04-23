from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import types
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """Declarative base class with common fields"""

    __name__: str
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self):
        return f"{type(self).__name__}[{self.id}]"
