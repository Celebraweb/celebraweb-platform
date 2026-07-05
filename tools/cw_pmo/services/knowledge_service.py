"""
CW PMO
Knowledge Service

Actualiza únicamente la sección
administrada por el PMO dentro
del Engineering Handbook.
"""

from core.paths import ENGINEERING


class KnowledgeService:

    def __init__(self):

        self.handbook = (
            ENGINEERING /
            "CW-500-Engineering-Handbook.md"
        )

    def load(self):

        content = self.handbook.read_text(
            encoding="utf-8"
        )

        return content

    def save(self, content):

        self.handbook.write_text(
            content,
            encoding="utf-8"
        )

    def update_pmo_section(self, new_section):

        content = self.load()

        start = "<!-- PMO:START -->"
        end = "<!-- PMO:END -->"

        if start not in content or end not in content:
            raise Exception(
                "La sección PMO no existe dentro del Engineering Handbook."
            )

        before = content.split(start)[0]
        after = content.split(end)[1]

        updated = before + start + "\n\n"
        updated += new_section
        updated += "\n\n" + end + after

        self.save(updated)