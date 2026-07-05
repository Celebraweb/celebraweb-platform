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