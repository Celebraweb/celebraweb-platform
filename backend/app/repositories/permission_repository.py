from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.schemas.permission import (
    PermissionCreate,
    PermissionUpdate,
)


class PermissionRepository:

    def get_all(
        self,
        db: Session,
    ):

        return db.query(Permission).all()

    def get_by_id(
        self,
        db: Session,
        permission_id: str,
    ):

        return (
            db.query(Permission)
            .filter(
                Permission.id == permission_id,
            )
            .first()
        )

    def get_by_code(
        self,
        db: Session,
        code: str,
    ):

        return (
            db.query(Permission)
            .filter(
                Permission.code == code,
            )
            .first()
        )

    def create(
        self,
        db: Session,
        permission: PermissionCreate,
    ):

        db_permission = Permission(

            code=permission.code,

            name=permission.name,

            description=permission.description,

        )

        db.add(db_permission)

        db.commit()

        db.refresh(db_permission)

        return db_permission

    def update(
        self,
        db: Session,
        permission_id: str,
        permission: PermissionUpdate,
    ):

        db_permission = self.get_by_id(
            db,
            permission_id,
        )

        if db_permission is None:
            return None

        data = permission.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():

            setattr(
                db_permission,
                key,
                value,
            )

        db.commit()

        db.refresh(db_permission)

        return db_permission

    def delete(
        self,
        db: Session,
        permission_id: str,
    ):

        db_permission = self.get_by_id(
            db,
            permission_id,
        )

        if db_permission is None:
            return False

        db.delete(db_permission)

        db.commit()

        return True