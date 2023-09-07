from pydantic import BaseModel, Field

from fast_api.documentation.openapi import OpenApiDocumentation

documentation = OpenApiDocumentation().load()


class RegisterRequest(BaseModel):
    user_id: str = Field(
        alias="user_id",
        description=documentation["api.register.user_id.description"],
        examples=["69c6420d-b180-469c-9d91-2ed6f8d353ae"],
        max_length=100,
    )
    role_id: str | None = Field(
        alias="client_id",
        default=None,
        description=documentation["api.register.role_id.description"],
        examples=["c40688fc-c81c-4bd5-a895-1a3168306d02"],
        max_length=100,
    )
    datetime: str | None = Field(
        alias="datetime",
        default=None,
        pattern=r"^\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?",
        description=documentation["api.register.datetime.description"],
        examples=["2023-09-04T14:05:12Z"],
    )
