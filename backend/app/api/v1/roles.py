from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse,
)
from app.services.role_service import RoleService

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)

service = RoleService()


@router.get(
    "/",
    response_model=list[RoleResponse],
)
def get_roles(
    db: Session = Depends(get_db),
):

    return service.get_all(db)


@router.get(
    "/{role_id}",
    response_model=RoleResponse,
)
def get_role(
    role_id: str,
    db: Session = Depends(get_db),
):

    role = service.get_by_id(
        db,
        role_id,
    )

    if role is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found",
        )

    return role


@router.post(
    "/",
    response_model=RoleResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
):

    try:

        return service.create(
            db,
            role,
        )

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )


@router.put(
    "/{role_id}",
    response_model=RoleResponse,
)
def update_role(
    role_id: str,
    role: RoleUpdate,
    db: Session = Depends(get_db),
):

    updated = service.update(
        db,
        role_id,
        role,
    )

    if updated is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found",
        )

    return updated


@router.delete(
    "/{role_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_role(
    role_id: str,
    db: Session = Depends(get_db),
):

    deleted = service.delete(
        db,
        role_id,
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found",
        )

    return