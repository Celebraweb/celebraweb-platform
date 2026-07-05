from fastapi import Depends

from app.dependencies.auth import get_current_user
from app.schemas.request_context import RequestContext


def get_request_context(
    current_user=Depends(get_current_user),
) -> RequestContext:

    return RequestContext(

        user_id=current_user.id,

        organization_id=current_user.organization_id,

        email=current_user.email,

        first_name=current_user.first_name,

        last_name=current_user.last_name,

        is_super_admin=current_user.is_super_admin,

        status=current_user.status,
    )