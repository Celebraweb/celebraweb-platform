"""
CW PMO
Validate Command

Realiza una validación básica del
estado del proyecto antes del cierre
de un Sprint.
"""

from services.project_service import ProjectService
from core.paths import ENGINEERING, SPRINTS


class ValidateCommand:

    def run(self):

        context = ProjectService().get_context()

        handbook = ENGINEERING / "CW-500-Engineering-Handbook.md"

        sprint_folder = SPRINTS / f"Sprint-{context.sprint:02d}"

        summary = sprint_folder / f"Sprint-{context.sprint:02d}-Summary.md"

        artifacts = sprint_folder / "Artifacts.md"

        print()
        print("=" * 50)
        print("      CW PMO - VALIDATE")
        print("=" * 50)
        print()

        checks = {
            "Manifest": True,
            "Engineering Handbook": handbook.exists(),
            "Artifacts": artifacts.exists(),
            "Sprint Summary": summary.exists(),
        }

        errors = 0

        for name, status in checks.items():

            result = "OK" if status else "ERROR"

            print(f"{name:.<30} {result}")

            if not status:
                errors += 1

        print()

        if errors == 0:
            print("VALIDACIÓN APROBADA")
        else:
            print(f"VALIDACIÓN FALLÓ ({errors} error(es))")

        print()
        print("=" * 50)