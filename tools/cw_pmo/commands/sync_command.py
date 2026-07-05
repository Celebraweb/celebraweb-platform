"""
CW PMO
Sync Command

Sincroniza y valida el estado de la
documentación del proyecto.
"""

from services.project_service import ProjectService
from core.paths import ENGINEERING, SPRINTS


class SyncCommand:

    def run(self):

        context = ProjectService().get_context()

        handbook = ENGINEERING / "CW-500-Engineering-Handbook.md"

        sprint_folder = SPRINTS / f"Sprint-{context.sprint:02d}"

        summary = sprint_folder / f"Sprint-{context.sprint:02d}-Summary.md"

        artifacts = sprint_folder / "Artifacts.md"

        print()
        print("=" * 50)
        print("           CW PMO - SYNC")
        print("=" * 50)
        print()

        print(
            f"PROJECT.yaml ............ {'OK' if context else 'ERROR'}"
        )

        print(
            f"Engineering Handbook .... {'OK' if handbook.exists() else 'ERROR'}"
        )

        print(
            f"Sprint Summary .......... {'OK' if summary.exists() else 'ERROR'}"
        )

        print(
            f"Artifacts ............... {'OK' if artifacts.exists() else 'ERROR'}"
        )

        print()

        print(f"Proyecto : {context.project}")
        print(f"Versión  : {context.version}")
        print(f"Sprint   : {context.sprint}")
        print(f"Estado   : {context.sprint_status}")

        print()
        print("=" * 50)