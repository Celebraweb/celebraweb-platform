from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class RoleResponse(RoleBase):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)