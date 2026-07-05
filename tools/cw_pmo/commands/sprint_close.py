"""
CW PMO
Sprint Close Command

Orquesta el cierre de un Sprint.
"""

from services.project_service import ProjectService
from services.generate_service import GenerateService
from services.backup_service import BackupService
from services.knowledge_service import KnowledgeService

from infrastructure.manifest_loader import ManifestLoader

from core.paths import ENGINEERING


class SprintCloseCommand:

    def execute(self):

        print()
        print("===================================")
        print("CW PMO - Sprint Close")
        print("===================================")

        project = ProjectService()
        generator = GenerateService()
        backup = BackupService()
        knowledge = KnowledgeService()

        context = project.get_context()

        sprint = context.sprint

        handbook = ENGINEERING / "CW-500-Engineering-Handbook.md"

        print("1. Generando documentación...")
        generator.run()

        print("2. Backup...")
        backup.backup(handbook)

        print("3. Actualizando PMO...")

        knowledge.update_pmo_section(
f"""
## Estado del Proyecto

Proyecto : {context.project}

Versión : {context.version}

Release : {context.release}

Fase : {context.phase}

Sprint : {context.sprint}

Nombre Sprint : {context.sprint_name}

Estado : Closed

Última actualización automática por CW PMO.
"""
        )

        print("4. Cerrando Sprint...")

        loader = ManifestLoader()

        manifest = loader.load()

        manifest["sprint"]["status"] = "Closed"

        loader.save(manifest)

        print()
        print(f"Sprint {sprint} cerrado correctamente.")