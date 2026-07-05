from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """
    Datos requeridos para iniciar sesión.
    """

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """
    OAuth2 Access Token
    """

    access_token: str
    token_type: str = "bearer"