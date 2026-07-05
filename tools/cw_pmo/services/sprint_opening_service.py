"""
CW PMO
Sprint Opening Service

Orquesta la ceremonia oficial
de apertura de un Sprint.
"""

from core.paths import GOVERNANCE, ENGINEERING, SPRINTS

from services.project_service import ProjectService
from services.document_reader import DocumentReader
from services.sprint_bootstrap_service import SprintBootstrapService


class SprintOpeningService:

    def run(self):

        context = ProjectService().get_context()

        # Garantiza la estructura documental del Sprint
        SprintBootstrapService().run()

        print()
        print("=" * 60)
        print("                 CELEBRAWEB PMO")
        print("=" * 60)
        print()
        print("SPRINT OPENING CEREMONY")
        print()

        print(f"Proyecto : {context.project}")
        print(f"Versión  : {context.version}")
        print(f"Release  : {context.release}")
        print(f"Fase     : {context.phase}")
        print(f"Sprint   : {context.sprint}")
        print(f"Estado   : {context.sprint_status}")

        print()
        print("-" * 60)
        print("DOCUMENTACIÓN")
        print("-" * 60)

        self._validate_documents(context)

        print()
        print("-" * 60)
        print("RESUMEN EJECUTIVO")
        print("-" * 60)

        print("Engineering Handbook ........ OK")
        print("Project Rules ............... OK")
        print("Decision Log ................. OK")
        print("Sprint Summary .............. OK")
        print("Artifacts ................... OK")

        print()
        print("=" * 60)
        print("READY")
        print()
        print("Puede iniciar la reunión de apertura.")
        print("=" * 60)

    def _validate_documents(self, context):

        sprint_folder = (
            SPRINTS /
            f"Sprint-{context.sprint:02d}"
        )

        documents = [

            (
                "PROJECT.yaml",
                GOVERNANCE / "PROJECT.yaml"
            ),

            (
                "Engineering Handbook",
                ENGINEERING / "CW-500-Engineering-Handbook.md"
            ),

            (
                "PROJECT-RULES.md",
                GOVERNANCE / "PROJECT-RULES.md"
            ),

            (
                "DECISION-LOG.md",
                GOVERNANCE / "DECISION-LOG.md"
            ),

            (
                "Sprint Summary",
                sprint_folder /
                f"Sprint-{context.sprint:02d}-Summary.md"
            ),

            (
                "Artifacts",
                sprint_folder /
                "Artifacts.md"
            )

        ]

        for name, path in documents:

            if DocumentReader.exists(path):

                print(f"✔ {name}")

            else:

                raise FileNotFoundError(
                    f"No existe: {path}"
                )