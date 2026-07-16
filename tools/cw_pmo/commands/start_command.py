"""
CW PMO
Start Command

Inicializa la ceremonia oficial
de apertura de un Sprint.
"""

from services.project_service import ProjectService
from services.sprint_opening_service import SprintOpeningService



class StartCommand:

    def run(self):
            
        project = ProjectService()

        project.open_next_sprint()

        SprintOpeningService().run()

        context = project.get_context()

        print()
        print("============================================================")
        print("CONTEXTO DEL SPRINT")
        print("============================================================")
        print()

        print(f"Producto              : {context.product}")
        print(f"Business Capability   : {context.capability_id}")
        print(f"Nombre                : {context.capability_name}")
        print(f"Dominio               : {context.capability_domain}")
        print()

        print("Objetivo del Sprint")
        print("-------------------")
        print(context.sprint_goal)
        print()

        print("Arquitectura")
        print("------------")
        print(f"Modelo de Capacidades : {context.capability_model}")
        print(f"Versión               : {context.capability_model_version}")

        print()
        print("============================================================")
        print("READY")
        print("============================================================")