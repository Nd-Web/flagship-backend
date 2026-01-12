from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models import User
from app.schemas.users import UserCreate, UserOut


class UsersService:
    def create_user(self, db: Session, payload: UserCreate) -> UserOut:
        # Optional but professional: prevent duplicate email
        existing = db.execute(select(User).where(User.email == payload.email)).scalar_one_or_none()
        if existing:
            # keep it simple for now (we'll upgrade to proper HTTP errors next)
            raise ValueError("Email already exists")

        user = User(name=payload.name, email=str(payload.email))
        db.add(user)
        db.commit()
        db.refresh(user)

        return UserOut(id=user.id, name=user.name, email=user.email)

    def list_users(self, db: Session) -> list[UserOut]:
        users = db.execute(select(User).order_by(User.id)).scalars().all()
        return [UserOut(id=u.id, name=u.name, email=u.email) for u in users]
