from sqlalchemy.orm import Session

from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


class OrganizationService:

    def __init__(self):

        self.repository = OrganizationRepository()

    def get_all(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        organization_id: str
    ):

        return self.repository.get_by_id(
            db,
            organization_id
        )

    def create(
        self,
        db: Session,
        organization: OrganizationCreate
    ):

        return self.repository.create(
            db,
            organization
        )

    def update(
        self,
        db: Session,
        organization_id: str,
        data: OrganizationUpdate
    ):

        organization = self.repository.get_by_id(
            db,
            organization_id
        )

        if organization is None:
            return None

        return self.repository.update(
            db,
            organization,
            data
        )

    def delete(
        self,
        db: Session,
        organization_id: str
    ):

        organization = self.repository.get_by_id(
            db,
            organization_id
        )

        if organization is None:
            return False

        self.repository.delete(
            db,
            organization
        )

        return True