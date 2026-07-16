from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.user_role import (
    UserRoleAssignment,
    UserRoleResponse,
)

from app.services.user_role_service import (
    UserRoleService,
)

router = APIRouter(
    prefix="/users",
    tags=["User Roles"],
)

service = UserRoleService()


@router.get(
    "/{user_id}/roles",
    response_model=list[UserRoleResponse],
)
def get_user_roles(
    user_id: str,
    db: Session = Depends(get_db),
):

    return service.get_roles(
        db,
        user_id,
    )


@router.put(
    "/{user_id}/roles",
    response_model=list[UserRoleResponse],
)
def replace_user_roles(
    user_id: str,
    assignment: UserRoleAssignment,
    db: Session = Depends(get_db),
):

    return service.replace_roles(
        db,
        user_id,
        assignment,
    )