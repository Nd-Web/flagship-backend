from fastapi import APIRouter
from app.schemas.echo import EchoRequest

router = APIRouter()

@router.post("/echo")
def echo(payload: EchoRequest):
    return {"message": f"Hello, {payload.name}!"}
