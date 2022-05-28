from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


class Authorization(object):
    algorithm: str = 'HS256'
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    scheme = OAuth2PasswordBearer(tokenUrl="token")


class Constants(object):
    authorization: Authorization = Authorization()
    lengths: dict = dict(strings=[64, 128, 256])
