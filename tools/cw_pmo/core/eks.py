"""
CW PMO
Enterprise Knowledge System (EKS)

Localiza la documentación oficial del proyecto.
"""

from pathlib import Path


class EKS:

    def __init__(self):

        # Ruta del PMO
        self.base_path = Path(__file__).resolve().parents[3]

        # Ruta de la documentación
        self.docs_path = self.base_path / "docs"

    def get_docs_path(self):

        return self.docs_path

    def exists(self):

        return self.docs_path.exists()