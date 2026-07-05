from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    code: str
    name: str
    legal_name: Optional[str] = None
    country: str
    timezone: str
    language: str = "es"


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    legal_name: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[str] = None
    language: Optional[str] = None
    status: Optional[str] = None


class OrganizationResponse(OrganizationBase):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)