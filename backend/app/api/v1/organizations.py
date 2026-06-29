from fastapi import APIRouter

from fastapi import APIRouter

from app.services.organization_service import OrganizationService

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)

service = OrganizationService()


@router.get("/")
def get_organizations():

    return service.get_all()