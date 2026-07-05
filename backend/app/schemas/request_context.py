from pydantic import BaseModel


class RequestContext(BaseModel):
    """
    Contexto del usuario autenticado.

    Este objeto desacopla la API y los servicios
    de las entidades ORM.
    """

    user_id: str

    organization_id: str

    email: str

    first_name: str

    last_name: str

    is_super_admin: bool

    status: str