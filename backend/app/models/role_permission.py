from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class RolePermission(BaseEntity):
    """
    Relación entre roles y permisos.

    Sprint 18 - Identity Engine
    """

    __tablename__ = "role_permissions"

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False,
    )

    permission_id: Mapped[str] = mapped_column(
        ForeignKey("permissions.id"),
        nullable=False,
    )