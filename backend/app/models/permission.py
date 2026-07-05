from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class Permission(BaseEntity):
    """
    Permiso del sistema.

    Sprint 10 - CW-204
    """

    __tablename__ = "permissions"

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )