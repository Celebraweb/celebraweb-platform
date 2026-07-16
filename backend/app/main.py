from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router
from app.api.v1.organizations import (
    router as organizations_router,
)
from app.api.v1.permissions import (
    router as permissions_router,
)
from app.api.v1.role_permissions import (
    router as role_permissions_router,
)
from app.api.v1.roles import (
    router as roles_router,
)
from app.api.v1.user_roles import (
    router as user_roles_router,
)
from app.api.v1.users import (
    router as users_router,
)

app = FastAPI(
    title="CelebraWeb Platform API",
    version="0.3.0",
)

# ------------------------------------------------------------------
# CORS
# ------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# API
# ------------------------------------------------------------------

app.include_router(
    organizations_router,
    prefix="/api/v1",
)

app.include_router(
    users_router,
    prefix="/api/v1",
)

app.include_router(
    roles_router,
    prefix="/api/v1",
)

app.include_router(
    permissions_router,
    prefix="/api/v1",
)

app.include_router(
    user_roles_router,
    prefix="/api/v1",
)

app.include_router(
    role_permissions_router,
    prefix="/api/v1",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

# ------------------------------------------------------------------
# Root
# ------------------------------------------------------------------

@app.get("/")
def root():

    return {
        "project": "CelebraWeb Platform",
        "status": "running",
        "version": "0.3.0",
    }