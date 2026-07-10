from sqlalchemy.orm import Session

from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


class RoleRepository:

    def get_all(
        self,
        db: Session,
    ):

        return db.query(Role).all()

    def get_by_id(
        self,
        db: Session,
        role_id: str,
    ):

        return (
            db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

    def get_by_code(
        self,
        db: Session,
        code: str,
    ):

        return (
            db.query(Role)
            .filter(Role.code == code)
            .first()
        )

    def create(
        self,
        db: Session,
        role: RoleCreate,
    ):

        db_role = Role(

            code=role.code,

            name=role.name,

            description=role.description,

        )

        db.add(db_role)

        db.commit()

        db.refresh(db_role)

        return db_role

    def update(
        self,
        db: Session,
        role_id: str,
        role: RoleUpdate,
    ):

        db_role = self.get_by_id(
            db,
            role_id,
        )

        if db_role is None:
            return None

        data = role.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():

            setattr(
                db_role,
                key,
                value,
            )

        db.commit()

        db.refresh(db_role)

        return db_role

    def delete(
        self,
        db: Session,
        role_id: str,
    ):

        db_role = self.get_by_id(
            db,
            role_id,
        )

        if db_role is None:
            return False

        db.delete(db_role)

        db.commit()

        return True