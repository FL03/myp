import random
import secrets
from typing import Optional

from pydantic import BaseModel

from app.utils.date import timestamp


class Item(BaseModel):
    label: str
    description: Optional[str]
    content: dict


class ItemIn(Item):
    id: str = secrets.token_hex(int(16 + random.randint(0, 16)))
    key: str = secrets.token_hex(int(16 + random.randint(0, 16))) + str(hash(timestamp()))
