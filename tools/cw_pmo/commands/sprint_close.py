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
        print("============================================================")
        print("                 CELEBRAWEB PMO")
        print("============================================================")
        print()
        print("SPRINT CLOSING CEREMONY")
        print()

        project = ProjectService()
        generator = GenerateService()
        backup = BackupService()
        knowledge = KnowledgeService()

        context = project.get_context()

        handbook = ENGINEERING / "CW-500-Engineering-Handbook.md"

        print("1. Generando documentación...")
        generator.run()

        print("2. Realizando backup...")
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

        #
        # Mensaje de commit
        #

        if getattr(context, "capability_name", ""):
            commit_message = (
                f"Sprint {context.sprint} - {context.capability_name}"
            )
        else:
            commit_message = (
                f"Sprint {context.sprint} - {context.sprint_name}"
            )

        print()
        print("============================================================")
        print("SPRINT CLOSED SUCCESSFULLY")
        print("============================================================")
        print()

        print(f"Proyecto : {context.project}")
        print(f"Versión  : {context.version}")
        print(f"Release  : {context.release}")
        print(f"Sprint   : {context.sprint}")
        print("Estado   : Closed")

        print()
        print("✓ Documentación generada")
        print("✓ Backup realizado")
        print("✓ PROJECT.yaml actualizado")
        print("✓ Sprint cerrado")

        print()
        print("============================================================")
        print("NEXT STEP - PUBLICAR EN GITHUB")
        print("============================================================")
        print()

        print("Paso 1 - Revisar los cambios detectados")
        print("---------------------------------------")
        print("git status")

        print()
        print("Paso 2 - Agregar los cambios al área de staging")
        print("-----------------------------------------------")
        print("git add .")

        print()
        print("Paso 3 - Verificar el área de staging")
        print("-------------------------------------")
        print("git status")

        print()
        print("Debe aparecer:")
        print("Changes to be committed")

        print()
        print("Paso 4 - Crear el commit")
        print("------------------------")
        print(f'git commit -m "{commit_message}"')

        print()
        print("Paso 5 - Publicar el Sprint")
        print("---------------------------")
        print("git push")

        print()
        print("============================================================")
        print("SPRINT COMPLETED")
        print("============================================================")