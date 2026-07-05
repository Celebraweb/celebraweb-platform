from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from app.core.settings import settings


class JWTService:
    """
    Platform JWT Service

    Responsabilidades:
    - Generar Access Tokens
    - Validar Access Tokens

    No conoce FastAPI.
    No conoce Base de Datos.
    No conoce Usuarios.
    """

    @classmethod
    def create_access_token(
        cls,
        data: dict[str, Any],
    ) -> str:

        to_encode = data.copy()

        expire = (
            datetime.now(timezone.utc)
            + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )

        to_encode.update(
            {
                "exp": expire
            }
        )

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

    @classmethod
    def verify_token(
        cls,
        token: str,
    ) -> dict[str, Any] | None:

        try:

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[
                    settings.JWT_ALGORITHM
                ],
            )

            return payload

        except JWTError:

            return None