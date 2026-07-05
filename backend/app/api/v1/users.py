from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies.request_context import get_request_context
from app.schemas.request_context import RequestContext
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

service = UserService()


@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_users(
    context: RequestContext = Depends(get_request_context),
    db: Session = Depends(get_db),
):

    return service.get_all_by_organization(
        db,
        context.organization_id,
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: str,
    context: RequestContext = Depends(get_request_context),
    db: Session = Depends(get_db),
):

    user = service.get_by_id(
        db,
        user_id,
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    context: RequestContext = Depends(get_request_context),
    db: Session = Depends(get_db),
):

    return service.create(
        db,
        user,
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: str,
    user: UserUpdate,
    context: RequestContext = Depends(get_request_context),
    db: Session = Depends(get_db),
):

    updated = service.update(
        db,
        user_id,
        user,
    )

    if updated is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return updated


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: str,
    context: RequestContext = Depends(get_request_context),
    db: Session = Depends(get_db),
):

    deleted = service.delete(
        db,
        user_id,
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return