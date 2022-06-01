import datetime
import secrets
from typing import List, Optional

from pydantic import BaseModel


class Account(BaseModel):
    account: str
    username: str
    keys: Optional[List[dict]]


class AccountStore(Account):
    id: str = secrets.token_hex(16)
    key: str = secrets.token_hex(16)
    hashed_password: str
    timestamp: str = str(datetime.datetime.now())
