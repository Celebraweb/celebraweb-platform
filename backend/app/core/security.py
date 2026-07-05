from passlib.context import CryptContext


class SecurityService:
    """
    Platform Security Service

    Responsabilidades:
    - Generar hashes de contraseñas
    - Verificar contraseñas

    No implementa autenticación,
    JWT ni autorización.
    """

    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    )

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(
        cls,
        plain_password: str,
        hashed_password: str,
    ) -> bool:

        return cls.pwd_context.verify(
            plain_password,
            hashed_password,
        )