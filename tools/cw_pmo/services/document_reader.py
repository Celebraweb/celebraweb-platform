"""
CW PMO
Document Reader

Lectura de documentos Markdown del PMO.
"""

from pathlib import Path


class DocumentReader:

    @staticmethod
    def exists(path: Path) -> bool:
        return path.exists()

    @staticmethod
    def load(path: Path) -> str:

        if not path.exists():
            raise FileNotFoundError(path)

        return path.read_text(
            encoding="utf-8"
        )