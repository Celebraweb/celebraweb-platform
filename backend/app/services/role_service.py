from sqlalchemy.orm import Session

from app.repositories.role_repository import RoleRepository
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
)


class RoleService:

    def __init__(self):

        self.repository = RoleRepository()

    def get_all(
        self,
        db: Session,
    ):

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        role_id: str,
    ):

        return self.repository.get_by_id(
            db,
            role_id,
        )

    def create(
        self,
        db: Session,
        role: RoleCreate,
    ):

        existing = self.repository.get_by_code(
            db,
            role.code,
        )

        if existing:

            raise ValueError(
                "Role code already exists."
            )

        return self.repository.create(
            db,
            role,
        )

    def update(
        self,
        db: Session,
        role_id: str,
        role: RoleUpdate,
    ):

        return self.repository.update(
            db,
            role_id,
            role,
        )

    def delete(
        self,
        db: Session,
        role_id: str,
    ):

        return self.repository.delete(
            db,
            role_id,
        )