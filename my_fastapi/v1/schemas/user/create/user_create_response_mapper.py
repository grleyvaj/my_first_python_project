from my_fastapi.v1.model.user_model import User
from my_fastapi.v1.schemas.user import UserCreateResponse


class UserCreateResponseMapper:
    def mapper(self: None, user: User) -> UserCreateResponse:
        return UserCreateResponse(
            id=user.id,
            username=user.username,
            email=user.email,
        )
