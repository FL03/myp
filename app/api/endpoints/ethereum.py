from fastapi import APIRouter
from pydantic import BaseModel

from app.core.session import session

db = session.deta.Base("user")
provider: session.provider = session.provider
router: APIRouter = APIRouter(prefix="/ethereum", tags=["ethereum"])


class Block(BaseModel):
    id: int


@router.get("/accounts")
async def accounts() -> dict:
    return dict(accounts=provider.eth.accounts)


@router.get("/current/block/number")
async def block_number() -> dict:
    return dict(block_number=provider.eth.block_number)


@router.get("/client/version")
async def client_version() -> dict:
    return dict(client_version=provider.clientVersion)


@router.get("/ens/to/{ens}")
async def ens_to_address(ens: str) -> dict:
    return dict(address=provider.ens.address(ens), ensname=ens)


@router.get("/ens/resolve/{ens}")
async def ens_to_address(ens: str, query: str = None):
    res = provider.ens.resolve(name=ens, get=query)
    return res
