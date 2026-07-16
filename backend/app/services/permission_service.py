from sqlalchemy.orm import Session

from app.repositories.permission_repository import (
    PermissionRepository,
)
from app.schemas.permission import (
    PermissionCreate,
    PermissionUpdate,
)


class PermissionService:

    def __init__(self):

        self.repository = PermissionRepository()

    def get_all(
        self,
        db: Session,
    ):

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        permission_id: str,
    ):

        return self.repository.get_by_id(
            db,
            permission_id,
        )

    def create(
        self,
        db: Session,
        permission: PermissionCreate,
    ):

        existing = self.repository.get_by_code(
            db,
            permission.code,
        )

        if existing:

            raise ValueError(
                "Permission code already exists."
            )

        return self.repository.create(
            db,
            permission,
        )

    def update(
        self,
        db: Session,
        permission_id: str,
        permission: PermissionUpdate,
    ):

        return self.repository.update(
            db,
            permission_id,
            permission,
        )

    def delete(
        self,
        db: Session,
        permission_id: str,
    ):

        return self.repository.delete(
            db,
            permission_id,
        )