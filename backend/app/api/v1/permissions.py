from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.permission import (
    PermissionCreate,
    PermissionUpdate,
    PermissionResponse,
)
from app.services.permission_service import (
    PermissionService,
)

router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"],
)

service = PermissionService()


@router.get(
    "/",
    response_model=list[PermissionResponse],
)
def get_permissions(
    db: Session = Depends(get_db),
):

    return service.get_all(db)


@router.get(
    "/{permission_id}",
    response_model=PermissionResponse,
)
def get_permission(
    permission_id: str,
    db: Session = Depends(get_db),
):

    permission = service.get_by_id(
        db,
        permission_id,
    )

    if permission is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found",
        )

    return permission


@router.post(
    "/",
    response_model=PermissionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_permission(
    permission: PermissionCreate,
    db: Session = Depends(get_db),
):

    try:

        return service.create(
            db,
            permission,
        )

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )


@router.put(
    "/{permission_id}",
    response_model=PermissionResponse,
)
def update_permission(
    permission_id: str,
    permission: PermissionUpdate,
    db: Session = Depends(get_db),
):

    updated = service.update(
        db,
        permission_id,
        permission,
    )

    if updated is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found",
        )

    return updated


@router.delete(
    "/{permission_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_permission(
    permission_id: str,
    db: Session = Depends(get_db),
):

    deleted = service.delete(
        db,
        permission_id,
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found",
        )

    return