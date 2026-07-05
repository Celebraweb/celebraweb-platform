"""
CW PMO
Generate Command

Genera automáticamente la documentación
administrativa del Sprint utilizando los
servicios del PMO.

Sprint 7
CW-701
"""

from services.generate_service import GenerateService


class GenerateCommand:

    def run(self):

        GenerateService().run()