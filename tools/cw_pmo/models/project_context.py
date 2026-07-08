"""
CW PMO
Project Context

Modelo del estado operativo
del proyecto.
"""

from dataclasses import dataclass


@dataclass
class ProjectContext:

    # ==========================================================
    # Proyecto
    # ==========================================================

    project: str
    version: str
    release: str
    phase: str

    # ==========================================================
    # Sprint
    # ==========================================================

    sprint: int
    sprint_name: str
    sprint_status: str

    # ==========================================================
    # Trabajo actual
    # ==========================================================

    product: str

    capability_id: str
    capability_name: str
    capability_domain: str

    sprint_goal: str

    # ==========================================================
    # Arquitectura
    # ==========================================================

    capability_model: str
    capability_model_version: str