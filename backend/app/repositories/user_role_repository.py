from sqlalchemy.orm import Session

from app.models.role import Role
from app.models.user_role import UserRole


class UserRoleRepository:

    def get_roles(
        self,
        db: Session,
        user_id: str,
    ):

        return (
            db.query(Role)
            .join(
                UserRole,
                UserRole.role_id == Role.id,
            )
            .filter(
                UserRole.user_id == user_id,
            )
            .all()
        )

    def replace_roles(
        self,
        db: Session,
        user_id: str,
        role_ids: list[str],
    ):

        (
            db.query(UserRole)
            .filter(
                UserRole.user_id == user_id,
            )
            .delete()
        )

        for role_id in role_ids:

            db.add(

                UserRole(
                    user_id=user_id,
                    role_id=role_id,
                )

            )

        db.commit()

        return self.get_roles(
            db,
            user_id,
        )