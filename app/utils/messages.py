from pydantic import BaseModel
from siwe import generate_nonce

from app.core.session import session
from app.utils.date import timestamp


class ConsoleMessage(BaseModel):
    message: str
    timestamp: str = timestamp()


class Siwe(BaseModel):
    address: str
    domain: str = "http://localhost:8080"
    chain_id: str = str(session.provider.eth.chain_id)
    nonce: str = generate_nonce()
    statement: str = "yes"
    uri: str = "http://localhost:8080/api/auth/"
    version: str = '1'


class Status(BaseModel):
    message: str
