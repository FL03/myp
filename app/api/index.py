from fastapi import APIRouter
from siwe import SiweMessage, ExpiredMessage, generate_nonce

from app.utils import ledgering
from .endpoints import ethereum, users

router: APIRouter = APIRouter(prefix="/api", tags=["default"])


@router.get("/nonce")
async def nonce() -> dict:
    return dict(nonce=generate_nonce(), timestamp=ledgering.timestamp())


@router.post("/verify")
async def verification(message, signature):
    siwe_message = SiweMessage(message=message)
    try:
        return siwe_message.verify(signature)
    except ExpiredMessage:
        print("MessageError: Expired")
    finally:
        print("Error")


router.include_router(router=ethereum.router)
router.include_router(router=users.router)
