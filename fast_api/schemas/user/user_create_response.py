from typing import Optional

from pydantic import Field

from fast_api.schemas.user.user_create_request import UserCreateRequest


class UserCreateResponse(UserCreateRequest):
    id: int = Field(default=1)
    credit_card_detail: bool = Field(default=None, omit_default=True)
