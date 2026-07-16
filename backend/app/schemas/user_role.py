from pydantic import BaseModel, ConfigDict


class UserRoleResponse(BaseModel):
    id: str
    code: str
    name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserRoleAssignment(BaseModel):
    role_ids: list[str]