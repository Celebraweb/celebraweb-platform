from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.core.jwt import JWTService
from app.database.database import get_db
from app.dependencies.request_context import get_request_context
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.schemas.request_context import RequestContext
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

service = AuthService()


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):

    user = service.authenticate(
        db,
        credentials.email,
        credentials.password,
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = JWTService.create_access_token(
        {
            "sub": user.id,
            "organization_id": user.organization_id,
            "email": user.email,
            "is_super_admin": user.is_super_admin,
        }
    )

    return TokenResponse(
        access_token=access_token
    )


@router.get(
    "/me",
    response_model=RequestContext,
)
def me(
    context: RequestContext = Depends(get_request_context),
):

    return context