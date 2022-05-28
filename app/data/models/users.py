from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    ensname: str
    disabled: Optional[bool]


class UserIn(User):
    hashed_password: str
