"""
CW PMO
Backup Service

Genera copias de seguridad de los
documentos antes de modificarlos.
"""

from datetime import datetime
import shutil

from core.paths import DOCS


class BackupService:

    def __init__(self):

        self.root = DOCS / "_backup"

    def backup(self, file_path):

        source = file_path

        if not source.exists():
            raise FileNotFoundError(source)

        today = datetime.now().strftime("%Y-%m-%d")

        destination = self.root / today

        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        target = destination / source.name

        shutil.copy2(source, target)

        print(f"Backup creado: {target}")

        return target