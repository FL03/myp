from datetime import timedelta, datetime

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from app.core.session import session
from app.data.models.tokens import TokenData
from app.data.models.users import User

constants = session.constants
db = session.deta.Base("users")


def verify_password(plain_password, hashed_password):
    return constants.authorization.context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return constants.authorization.context.hash(password)


def get_user(ensname: str):
    for user in db.fetch().items:
        if user["ensname"] == ensname:
            return db.get(user["key"])
        else:
            return None


def authenticate_user(username: str, password: str):
    user = get_user(ensname=username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, session.settings.api_token, algorithm=constants.authorization.algorithm)
    return encoded_jwt


async def get_current_user(token: str = Depends(constants.authorization.scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, session.settings.api_token, algorithms=[constants.authorization.algorithm])
        ensname: str = payload.get("sub")
        if ensname is None:
            raise credentials_exception
        token_data = TokenData(ensname=ensname)
    except JWTError:
        raise credentials_exception
    user = get_user(ensname=token_data.ensname)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def decode_token(user_key):
    user = get_user(user_key)
    return user