from sqlalchemy import String, Text

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_entity import BaseEntity


class AuditLog(BaseEntity):
    """
    Registro de auditoría de la plataforma.

    Sprint 10 - CW-205
    """

    __tablename__ = "audit_logs"

    organization_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    user_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    entity: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    entity_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
    )

    details: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )