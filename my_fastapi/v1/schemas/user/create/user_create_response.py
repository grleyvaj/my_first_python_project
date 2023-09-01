from pydantic import Field

from my_fastapi.v1.schemas.user import UserCreateRequest


class UserCreateResponse(UserCreateRequest):
    id: int = Field(default=1)
