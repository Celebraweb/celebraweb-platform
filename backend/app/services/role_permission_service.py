from sqlalchemy.orm import Session

from app.repositories.role_permission_repository import (
    RolePermissionRepository,
)
from app.schemas.role_permission import (
    RolePermissionAssignment,
)


class RolePermissionService:

    def __init__(self):

        self.repository = RolePermissionRepository()

    def get_permissions(
        self,
        db: Session,
        role_id: str,
    ):

        return self.repository.get_permissions(
            db,
            role_id,
        )

    def replace_permissions(
        self,
        db: Session,
        role_id: str,
        assignment: RolePermissionAssignment,
    ):

        return self.repository.replace_permissions(
            db,
            role_id,
            assignment.permission_ids,
        )