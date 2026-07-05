from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from app.services.organization_service import OrganizationService

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)

service = OrganizationService()


@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def get_organizations(
    db: Session = Depends(get_db),
):

    return service.get_all(db)


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization(
    organization_id: str,
    db: Session = Depends(get_db),
):

    organization = service.get_by_id(
        db,
        organization_id,
    )

    if organization is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    return organization


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
):

    return service.create(
        db,
        organization,
    )


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def update_organization(
    organization_id: str,
    organization: OrganizationUpdate,
    db: Session = Depends(get_db),
):

    updated = service.update(
        db,
        organization_id,
        organization,
    )

    if updated is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    return updated


@router.delete(
    "/{organization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_organization(
    organization_id: str,
    db: Session = Depends(get_db),
):

    deleted = service.delete(
        db,
        organization_id,
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    return