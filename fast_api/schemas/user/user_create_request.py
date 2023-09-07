from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    username: str = Field(example="gloria2023", min_length=8, max_length=50)
    email: Optional[str] = Field(example="glorialj@gmail.com", min_length=8, max_length=50)
    is_active: Optional[bool] = Field(default=True)
    register_date: datetime
