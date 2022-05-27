import random
import secrets

from pydantic import BaseModel

from ..utils.ledgering import timestamp


class ConsoleMessage(BaseModel):
    id: float = random.Random()
    key: str = secrets.token_hex()
    message: str
    timestamp: str = timestamp()


class Block(BaseModel):
    id: int
    hash: str
    nonce: str
    previous_hash: str
    timestamp: str = timestamp()
