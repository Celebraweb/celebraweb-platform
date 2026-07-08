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

            # ==========================================================
            # Proyecto
            # ==========================================================

            project=self.data["project"]["name"],
            version=self.data["project"]["version"],
            release=self.data["release"]["current"],
            phase=self.data["lifecycle"]["phase"],

            # ==========================================================
            # Sprint
            # ==========================================================

            sprint=self.data["sprint"]["current"],
            sprint_name=self.data["sprint"]["name"],
            sprint_status=self.data["sprint"]["status"],

            # ==========================================================
            # Trabajo actual
            # ==========================================================

            product=self.data["current_work"]["product"],

            capability_id=self.data["current_work"]["capability"]["id"],
            capability_name=self.data["current_work"]["capability"]["name"],
            capability_domain=self.data["current_work"]["capability"]["domain"],

            sprint_goal=self.data["current_work"]["sprint_goal"],

            # ==========================================================
            # Arquitectura
            # ==========================================================

            capability_model=self.data["architecture"]["capability_model"]["document"],
            capability_model_version=self.data["architecture"]["capability_model"]["version"],
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

            # ==========================================================
            # Proyecto
            # ==========================================================

            project=self.data["project"]["name"],
            version=self.data["project"]["version"],
            release=self.data["release"]["current"],
            phase=self.data["lifecycle"]["phase"],

            # ==========================================================
            # Sprint
            # ==========================================================

            sprint=self.data["sprint"]["current"],
            sprint_name=self.data["sprint"]["name"],
            sprint_status=self.data["sprint"]["status"],

            # ==========================================================
            # Trabajo actual
            # ==========================================================

            product=self.data["current_work"]["product"],

            capability_id=self.data["current_work"]["capability"]["id"],
            capability_name=self.data["current_work"]["capability"]["name"],
            capability_domain=self.data["current_work"]["capability"]["domain"],

            sprint_goal=self.data["current_work"]["sprint_goal"],

            # ==========================================================
            # Arquitectura
            # ==========================================================

            capability_model=self.data["architecture"]["capability_model"]["document"],
            capability_model_version=self.data["architecture"]["capability_model"]["version"],
        )

        return self.context