from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


class EchoRequest(BaseModel):
    name: str


@app.post("/echo")
def echo(payload: EchoRequest):
    return {"message": f"Hello, {payload.name}!"}


# ---------------------------
# Day 3: In-memory Users API
# ---------------------------

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr


# In-memory "database"
_users: list[UserOut] = []
_next_user_id = 1


@app.post("/users", response_model=UserOut, status_code=201)
def create_user(payload: UserCreate):
    global _next_user_id

    user = UserOut(
        id=_next_user_id,
        name=payload.name,
        email=payload.email,
    )
    _next_user_id += 1
    _users.append(user)
    return user


@app.get("/users", response_model=list[UserOut])
def list_users():
    return _users
