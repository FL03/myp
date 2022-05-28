from fastapi import APIRouter
from siwe import SiweMessage, ExpiredMessage, generate_nonce

from app.api.endpoints import auth, ethereum, users
from app.core.session import session
from app.utils import messages

router: APIRouter = APIRouter(prefix="/api", tags=["default"])


@router.get("/nonce")
async def get_nonce() -> str:
    return generate_nonce()


@router.post("/verify/{ensname}")
async def verification(ensname: str):
    message = SiweMessage(message=messages.Siwe(address=session.provider.ens.address(ensname)).dict())
    try:
        return message.prepare_message()
    except ExpiredMessage:
        print("MessageError: Expired")
    finally:
        print("Error")


router.include_router(router=auth.router)
router.include_router(router=ethereum.router)
router.include_router(router=users.router)
