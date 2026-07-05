"""
CW PMO
Project Context

Modelo del estado operativo
del proyecto.
"""

from dataclasses import dataclass


@dataclass
class ProjectContext:

    project: str
    version: str

    sprint: int
    sprint_name: str
    sprint_status: str

    phase: str

    release: str