import datetime
import secrets
from typing import Optional

from pydantic import BaseModel


class Component(BaseModel):
    background: Optional[str] = "#FFFFFF"
    border: Optional[str] = "#000000"
    color: Optional[str] = "#000000"
    class_name: Optional[str]
    label: str
    data: Optional[list]


class ComponentStore(Component):
    id: str = secrets.token_hex(16)
    key: str = secrets.token_hex(16)
    timestamp: str = str(datetime.datetime.now())
