from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.role_permission import (
    RolePermissionAssignment,
    RolePermissionResponse,
)

from app.services.role_permission_service import (
    RolePermissionService,
)

router = APIRouter(
    prefix="/roles",
    tags=["Role Permissions"],
)

service = RolePermissionService()


@router.get(
    "/{role_id}/permissions",
    response_model=list[RolePermissionResponse],
)
def get_role_permissions(
    role_id: str,
    db: Session = Depends(get_db),
):

    return service.get_permissions(
        db,
        role_id,
    )


@router.put(
    "/{role_id}/permissions",
    response_model=list[RolePermissionResponse],
)
def replace_role_permissions(
    role_id: str,
    assignment: RolePermissionAssignment,
    db: Session = Depends(get_db),
):

    return service.replace_permissions(
        db,
        role_id,
        assignment,
    )