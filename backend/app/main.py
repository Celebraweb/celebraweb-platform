from fastapi import FastAPI

from app.api.v1.organizations import router as organizations_router

app = FastAPI(
    title="CelebraWeb API",
    version="0.1.0"
)

app.include_router(
    organizations_router,
    prefix="/api/v1"
)

@app.get("/")
def root():
    return {
        "product": "CelebraWeb",
        "version": "0.1.0",
        "status": "online"
    }