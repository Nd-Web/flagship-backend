from app.schemas.users import UserCreate, UserOut


class UsersService:
    def __init__(self) -> None:
        self._users: list[UserOut] = []
        self._next_user_id = 1

    def create_user(self, payload: UserCreate) -> UserOut:
        user = UserOut(
            id=self._next_user_id,
            name=payload.name,
            email=payload.email,
        )
        self._next_user_id += 1
        self._users.append(user)
        return user

    def list_users(self) -> list[UserOut]:
        return self._users
