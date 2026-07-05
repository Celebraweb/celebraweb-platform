"""
CW PMO
Artifact Service

Administra los artefactos generados
durante cada Sprint.
"""

from core.paths import SPRINTS


class ArtifactService:

    def __init__(self):

        self.docs = SPRINTS

    def create_sprint_folder(self, sprint):

        folder = self.docs / f"Sprint-{sprint:02d}"

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # Garantiza el índice de artefactos
        artifacts = folder / "Artifacts.md"

        if not artifacts.exists():

            artifacts.write_text(
f"""# Artifacts - Sprint {sprint}

Listado de artefactos generados durante el Sprint.

---

""",
encoding="utf-8")

        return folder

    def create_summary(self, sprint):

        folder = self.create_sprint_folder(sprint)

        summary = folder / f"Sprint-{sprint:02d}-Summary.md"

        if not summary.exists():

            summary.write_text(
f"""# Sprint {sprint}

## Objetivo

Pendiente.

---

## Componentes implementados

-

---

## Resultado

Pendiente.

---

## Artefactos

-

""",
encoding="utf-8")

        return summary

    def register_artifact(self, sprint, filename):

        folder = self.create_sprint_folder(sprint)

        index = folder / "Artifacts.md"

        with open(
            index,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(f"- {filename}\n")

    def list_artifacts(self, sprint):

        folder = self.create_sprint_folder(sprint)

        return list(folder.iterdir())