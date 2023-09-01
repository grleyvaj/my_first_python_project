from my_fastapi.v1.model.user_model import User
from my_fastapi.v1.schemas.user import UserCreateRequest


class UserService:

    def create(self: None, user_input: UserCreateRequest) -> User:
        return User.create(
            username=user_input.username,
            email=user_input.email,
        )

    def get_user(self: None, identifier: int) -> User | None:
        user = User.select().where(User.id == identifier).first()

        return user if user else None

    def delete(self: None, user: User) -> None:
        user.delete_instance()
