from sqlalchemy.orm import Session

from app.core.security import SecurityService
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    def __init__(self):

        self.repository = UserRepository()

    def get_all(
        self,
        db: Session,
    ):

        return self.repository.get_all(db)

    def get_all_by_organization(
        self,
        db: Session,
        organization_id: str,
    ):

        return self.repository.get_all_by_organization(
            db,
            organization_id,
        )

    def get_by_id(
        self,
        db: Session,
        user_id: str,
    ):

        return self.repository.get_by_id(
            db,
            user_id,
        )

    def create(
        self,
        db: Session,
        user: UserCreate,
    ):

        user.password = SecurityService.hash_password(
            user.password
        )

        return self.repository.create(
            db,
            user,
        )

    def update(
        self,
        db: Session,
        user_id: str,
        user: UserUpdate,
    ):

        if user.password is not None:

            user.password = SecurityService.hash_password(
                user.password
            )

        return self.repository.update(
            db,
            user_id,
            user,
        )

    def delete(
        self,
        db: Session,
        user_id: str,
    ):

        return self.repository.delete(
            db,
            user_id,
        )