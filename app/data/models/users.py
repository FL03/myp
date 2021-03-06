import datetime
import secrets
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    disabled: Optional[bool]


class UserIn(User):
    id: str = secrets.token_hex(16)
    key: str = secrets.token_hex(16)
    timestamp: str = str(datetime.datetime.now())
    hashed_password: str
