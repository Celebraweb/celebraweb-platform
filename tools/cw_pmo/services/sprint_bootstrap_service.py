"""
CW PMO
Sprint Bootstrap Service

Garantiza la existencia de la estructura documental
del Sprint antes de iniciar la ceremonia de apertura.
"""

from core.paths import SPRINTS

from services.project_service import ProjectService


class SprintBootstrapService:

    def run(self):

        context = ProjectService().get_context()

        sprint_folder = (
            SPRINTS /
            f"Sprint-{context.sprint:02d}"
        )

        sprint_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        summary = (
            sprint_folder /
            f"Sprint-{context.sprint:02d}-Summary.md"
        )

        if not summary.exists():

            summary.write_text(
f"""# Sprint {context.sprint:02d} Summary

## Objetivo

Pendiente de completar.

---

## Historias del Sprint

Pendiente.

---

## Resultados

Pendiente.
""",
                encoding="utf-8"
            )

        artifacts = (
            sprint_folder /
            "Artifacts.md"
        )

        if not artifacts.exists():

            artifacts.write_text(
"""# Artifacts

## Artefactos generados durante el Sprint

Pendiente.
""",
                encoding="utf-8"
            )