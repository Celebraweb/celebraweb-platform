from services.backup_service import BackupService

service = BackupService()

service.backup(
    "../../docs/06-Engineering/CW-500-Engineering-Handbook.md"
)