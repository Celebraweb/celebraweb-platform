"""
CW PMO
Manifest Loader

Responsable de localizar, cargar
y guardar el PROJECT.yaml del proyecto.
"""

from pathlib import Path

import yaml


class ManifestLoader:

    def __init__(self):

        self.root = Path(__file__).resolve().parents[3]

        self.manifest = (
            self.root /
            "docs" /
            "00-Governance" /
            "PROJECT.yaml"
        )

    def load(self):

        if not self.manifest.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {self.manifest}"
            )

        with open(
            self.manifest,
            "r",
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)

    def save(self, data):

        with open(
            self.manifest,
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                data,
                file,
                sort_keys=False,
                allow_unicode=True
            )