from fast_api.model.user_model import User
from fast_api.schemas.user.user_create_response import UserCreateResponse


class UserCreateResponseMapper:
    def mapper(self: None, user: User) -> UserCreateResponse:
        return UserCreateResponse(
            id=user.id,
            username=user.username,
            email=user.email,
        )
