from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class UserRole(BaseEntity):
    """
    Relación entre usuarios y roles.

    Sprint 10 - CW-204
    """

    __tablename__ = "user_roles"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False,
    )