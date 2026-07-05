"""
CW PMO
Project Service
"""

from infrastructure.manifest_loader import ManifestLoader
from models.project_context import ProjectContext


class ProjectService:

    def __init__(self):

        self.loader = ManifestLoader()

        self.data = self.loader.load()

        self.context = ProjectContext(

            project=self.data["project"]["name"],
            version=self.data["project"]["version"],

            sprint=self.data["sprint"]["current"],
            sprint_name=self.data["sprint"]["name"],
            sprint_status=self.data["sprint"]["status"],

            phase=self.data["lifecycle"]["phase"],

            release=self.data["release"]["current"],
        )

    def get_context(self):

        return self.context

    def open_next_sprint(self):

        if self.data["sprint"]["status"] != "Closed":
            return self.context

        next_sprint = self.data["sprint"]["current"] + 1

        self.data["sprint"]["current"] = next_sprint
        self.data["sprint"]["name"] = f"Sprint {next_sprint}"
        self.data["sprint"]["status"] = "In Progress"

        self.loader.save(self.data)

        self.context = ProjectContext(

            project=self.data["project"]["name"],
            version=self.data["project"]["version"],

            sprint=self.data["sprint"]["current"],
            sprint_name=self.data["sprint"]["name"],
            sprint_status=self.data["sprint"]["status"],

            phase=self.data["lifecycle"]["phase"],

            release=self.data["release"]["current"],
        )

        return self.context