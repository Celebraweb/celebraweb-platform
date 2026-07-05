from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class User(BaseEntity):
    __tablename__ = "users"

    organization_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("organizations.id"),
        nullable=False
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_super_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )