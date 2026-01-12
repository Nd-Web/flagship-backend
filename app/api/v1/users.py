from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.db.session import get_db
from app.schemas.users import UserCreate, UserOut
from app.services.users_service import UsersService

router = APIRouter()
users_service = UsersService()


@router.post("/users", response_model=UserOut, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        return users_service.create_user(db, payload)
    except ValueError as e:
        # simple, correct behavior for duplicates
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return users_service.list_users(db)
