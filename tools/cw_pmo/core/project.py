"""
CW PMO
Project Core

Responsable de administrar la información general
del proyecto CelebraWeb.
"""

from dataclasses import dataclass


@dataclass
class ProjectInfo:
    """Información general del proyecto."""

    name: str
    version: str
    sprint: str
    status: str
    objective: str


class Project:

    def get_info(self) -> ProjectInfo:

        return ProjectInfo(
            name="CelebraWeb Platform",
            version="0.2.0",
            sprint="Sprint 4",
            status="En Cierre",
            objective="Persistencia con PostgreSQL y Alembic"
        )