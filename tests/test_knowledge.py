from services.knowledge_service import KnowledgeService

service = KnowledgeService()

service.update_pmo_section(
"""
## Estado del Proyecto

Proyecto: CelebraWeb

Sprint: 5

Estado: Desarrollo

Versión: 0.2.0
"""
)

print("PMO actualizado correctamente.")