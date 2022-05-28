from fastapi import APIRouter
from siwe import SiweMessage, ExpiredMessage, generate_nonce

from app.api.endpoints import ethereum, users
from app.core.session import session
from app.utils import messages

router: APIRouter = APIRouter(prefix="/api", tags=["default"])


@router.get("/auth/nonce", tags=["auth"])
async def get_nonce() -> str:
    return generate_nonce()


@router.post("/auth/verify/{ensname}", tags=["auth"])
async def verification(ensname: str):
    message = SiweMessage(message=messages.Siwe(address=session.provider.ens.address(ensname)).dict())
    try:
        return message.prepare_message()
    except ExpiredMessage:
        print("MessageError: Expired")
    finally:
        print("Error")


router.include_router(router=ethereum.router)
router.include_router(router=users.router)
