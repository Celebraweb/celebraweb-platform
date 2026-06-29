class OrganizationRepository:

    def get_all(self):
        return [
            {
                "id": 1,
                "name": "CelebraWeb Demo",
                "country": "Colombia",
                "status": "ACTIVE"
            }
        ]