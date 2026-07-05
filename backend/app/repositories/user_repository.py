from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:

    def get_all(
        self,
        db: Session,
    ):

        return db.query(User).all()

    def get_all_by_organization(
        self,
        db: Session,
        organization_id: str,
    ):

        return (
            db.query(User)
            .filter(
                User.organization_id == organization_id
            )
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        user_id: str,
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str,
    ):

        return (
            db.query(User)
            .filter(User.email == email.lower())
            .first()
        )

    def create(
        self,
        db: Session,
        user: UserCreate,
    ):

        db_user = User(

            organization_id=user.organization_id,

            first_name=user.first_name,

            last_name=user.last_name,

            email=user.email.lower(),

            # El Service ya entrega el hash
            password_hash=user.password,

            is_super_admin=user.is_super_admin,

            email_verified=user.email_verified

        )

        db.add(db_user)

        db.commit()

        db.refresh(db_user)

        return db_user

    def update(
        self,
        db: Session,
        user_id: str,
        user: UserUpdate,
    ):

        db_user = self.get_by_id(
            db,
            user_id,
        )

        if db_user is None:

            return None

        data = user.model_dump(
            exclude_unset=True
        )

        if "password" in data:

            # El Service ya entrega el hash
            data["password_hash"] = data.pop(
                "password"
            )

        if "email" in data:

            data["email"] = data["email"].lower()

        for key, value in data.items():

            setattr(
                db_user,
                key,
                value,
            )

        db.commit()

        db.refresh(db_user)

        return db_user

    def delete(
        self,
        db: Session,
        user_id: str,
    ):

        db_user = self.get_by_id(
            db,
            user_id,
        )

        if db_user is None:

            return False

        db.delete(db_user)

        db.commit()

        return True
    