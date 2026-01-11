from fastapi import APIRouter
from app.schemas.users import UserCreate, UserOut
from app.services.users_service import UsersService

router = APIRouter()

users_service = UsersService()

@router.post("/users", response_model=UserOut, status_code=201)
def create_user(payload: UserCreate):
    return users_service.create_user(payload)

@router.get("/users", response_model=list[UserOut])
def list_users():
    return users_service.list_users()
