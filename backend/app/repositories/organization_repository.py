from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


class OrganizationRepository:

    def get_all(
        self,
        db: Session
    ):

        return db.query(Organization).all()

    def get_by_id(
        self,
        db: Session,
        organization_id: str
    ):

        return (
            db.query(Organization)
            .filter(
                Organization.id == organization_id
            )
            .first()
        )

    def create(
        self,
        db: Session,
        organization: OrganizationCreate
    ):

        db_organization = Organization(

            code=organization.code.upper(),
            name=organization.name,
            legal_name=organization.legal_name,
            country=organization.country,
            timezone=organization.timezone,
            language=organization.language

        )

        db.add(db_organization)

        db.commit()

        db.refresh(db_organization)

        return db_organization

    def update(
        self,
        db: Session,
        organization: Organization,
        data: OrganizationUpdate
    ):

        update_data = data.model_dump(exclude_unset=True)

        if "code" in update_data and update_data["code"] is not None:
            update_data["code"] = update_data["code"].upper()

        for field, value in update_data.items():
            setattr(
                organization,
                field,
                value
            )

        db.commit()

        db.refresh(organization)

        return organization

    def delete(
        self,
        db: Session,
        organization: Organization
    ):

        db.delete(organization)

        db.commit()