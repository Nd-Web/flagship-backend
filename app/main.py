from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.echo import router as echo_router
from app.api.v1.users import router as users_router

app = FastAPI(title="Flagship Backend")

app.include_router(health_router)
app.include_router(echo_router)
app.include_router(users_router)
