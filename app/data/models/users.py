from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    disabled: Optional[bool]


class UserIn(User):
    hashed_password: str
