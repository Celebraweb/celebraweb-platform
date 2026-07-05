from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class Organization(BaseEntity):
    __tablename__ = "organizations"

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    legal_name: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    timezone: Mapped[str] = mapped_column(
        String(60),
        nullable=False
    )

    language: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="es"
    )