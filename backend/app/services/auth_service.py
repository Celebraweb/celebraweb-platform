from sqlalchemy.orm import Session

from app.core.security import SecurityService
from app.repositories.user_repository import UserRepository


class AuthService:
    """
    Authentication Service

    Responsabilidades:
    - Autenticar usuarios
    - Verificar credenciales

    No genera JWT.
    No administra usuarios.
    """

    def __init__(self):

        self.repository = UserRepository()

    def authenticate(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = self.repository.get_by_email(
            db,
            email,
        )

        if user is None:

            return None

        if user.status != "ACTIVE":

            return None

        if not SecurityService.verify_password(
            password,
            user.password_hash,
        ):

            return None

        return user