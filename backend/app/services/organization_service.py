from app.repositories.organization_repository import OrganizationRepository


class OrganizationService:

    def __init__(self):

        self.repository = OrganizationRepository()

    def get_all(self):

        return self.repository.get_all()
