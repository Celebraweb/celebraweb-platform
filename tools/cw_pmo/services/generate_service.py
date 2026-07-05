"""
CW PMO
Generate Service

Orquesta la generación automática
de la documentación administrativa
del Sprint.

Sprint 7
CW-701
"""

from pathlib import Path

from core.paths import SPRINTS

from services.project_service import ProjectService
from services.artifact_service import ArtifactService
from services.knowledge_service import KnowledgeService


class GenerateService:

    def __init__(self):

        self.project = ProjectService()
        self.artifacts = ArtifactService()
        self.knowledge = KnowledgeService()

    def run(self):

        context = self.project.get_context()

        print()
        print("=" * 60)
        print("          CW PMO - GENERATE")
        print("=" * 60)
        print()

        print(
            f"Generando documentación del Sprint {context.sprint}"
        )

        # Garantiza estructura del Sprint
        self.artifacts.create_sprint_folder(
            context.sprint
        )

        self.artifacts.create_summary(
            context.sprint
        )

        # Completa automáticamente el Summary
        self._generate_summary(context)

        print("✔ Sprint Summary")

        print("✔ Artifacts")

        print()
        print("=" * 60)
        print("GENERATE FINALIZADO")
        print("=" * 60)

    def _generate_summary(self, context):

        summary = (
            SPRINTS
            / f"Sprint-{context.sprint:02d}"
            / f"Sprint-{context.sprint:02d}-Summary.md"
        )

        content = f"""# Sprint {context.sprint:02d} Summary

---

## Proyecto

**Proyecto:** {context.project}

**Versión:** {context.version}

**Release:** {context.release}

**Fase:** {context.phase}

**Sprint:** {context.sprint}

**Estado:** {context.sprint_status}

---

## Objetivo del Sprint

Pendiente de definición.

---

## Componentes implementados

Pendiente.

---

## Artefactos

Ver Artifacts.md

---

## Resultado

En progreso.

"""

        summary.write_text(
            content,
            encoding="utf-8"
        )