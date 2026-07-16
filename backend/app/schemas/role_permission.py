from pydantic import BaseModel, ConfigDict


class RolePermissionResponse(BaseModel):
    id: str
    code: str
    name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class RolePermissionAssignment(BaseModel):
    permission_ids: list[str]