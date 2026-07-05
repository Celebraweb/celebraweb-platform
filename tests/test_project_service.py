from services.project_service import ProjectService

service = ProjectService()

context = service.get_context()

print()

print(context)

print()

print(context.project)

print(context.version)

print(context.sprint)

print(context.phase)