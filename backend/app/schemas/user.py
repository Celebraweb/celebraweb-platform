from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    organization_id: str
    first_name: str
    last_name: str
    email: EmailStr
    is_super_admin: bool = False
    email_verified: bool = False


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_super_admin: Optional[bool] = None
    email_verified: Optional[bool] = None
    status: Optional[str] = None


class UserResponse(UserBase):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)