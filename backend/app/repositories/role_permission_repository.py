from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.models.role_permission import RolePermission


class RolePermissionRepository:

    def get_permissions(
        self,
        db: Session,
        role_id: str,
    ):

        return (
            db.query(Permission)
            .join(
                RolePermission,
                RolePermission.permission_id == Permission.id,
            )
            .filter(
                RolePermission.role_id == role_id,
            )
            .all()
        )

    def replace_permissions(
        self,
        db: Session,
        role_id: str,
        permission_ids: list[str],
    ):

        (
            db.query(RolePermission)
            .filter(
                RolePermission.role_id == role_id,
            )
            .delete()
        )

        for permission_id in permission_ids:

            db.add(

                RolePermission(
                    role_id=role_id,
                    permission_id=permission_id,
                )

            )

        db.commit()

        return self.get_permissions(
            db,
            role_id,
        )