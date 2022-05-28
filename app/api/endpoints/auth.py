from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from siwe.siwe import SiweMessage, ExpiredMessage, MalformedSession, generate_nonce

from app.core.session import session
from app.data.models.tokens import Token
from app.utils import messages
from app.utils.users import authenticate_user, create_access_token

constants = session.constants
db = session.deta.Base("users")
router: APIRouter = APIRouter(prefix="/oauth", tags=["auth"])


@router.post("/siwe/message")
async def create_message(ensname: str):
    msg = SiweMessage(
        message=messages.Siwe(address=session.provider.ens.address(ensname), nonce=generate_nonce()).dict())
    return msg.prepare_message()


@router.get("/siwe/nonce")
async def get_nonce() -> str:
    return generate_nonce()


@router.post("/siwe/verify")
async def verification(ensname: str):
    message = SiweMessage(message=messages.Siwe(address=session.provider.ens.address(ensname)).dict())
    try:
        return message.prepare_message()
    except ExpiredMessage:
        print("MessageError: Expired")
    except MalformedSession:
        print("Error: MalformedSession")
    finally:
        print("Error")


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=constants.authorization.expiration)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
