import datetime
import secrets
from typing import Optional

from pydantic import BaseModel


class Profile(BaseModel):
    prefix_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]


class ProfileStore(Profile):
    id: str = secrets.token_hex(16)
    key: str = secrets.token_hex(16)
    timestamp: str = str(datetime.datetime.now())
