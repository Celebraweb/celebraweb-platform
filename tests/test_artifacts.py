from services.artifact_service import ArtifactService

service = ArtifactService()

service.create_summary(5)

service.register_artifact(5, "Architecture.md")

service.register_artifact(5, "Docker-Report.md")

print(service.list_artifacts(5))