from pydantic import BaseModel, Field


class PersonRequestModel(BaseModel):
    username: str = Field(example="grleyva", min_length=8)
    email: str = Field(example="grleyva@gmail.com", min_length=8)
