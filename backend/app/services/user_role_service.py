from sqlalchemy.orm import Session

from app.repositories.user_role_repository import (
    UserRoleRepository,
)
from app.schemas.user_role import (
    UserRoleAssignment,
)


class UserRoleService:

    def __init__(self):

        self.repository = UserRoleRepository()

    def get_roles(
        self,
        db: Session,
        user_id: str,
    ):

        return self.repository.get_roles(
            db,
            user_id,
        )

    def replace_roles(
        self,
        db: Session,
        user_id: str,
        assignment: UserRoleAssignment,
    ):

        return self.repository.replace_roles(
            db,
            user_id,
            assignment.role_ids,
        )