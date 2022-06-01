from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


class Authorization(object):
    algorithm: str = 'HS256'
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    expiration: int = 30
    scheme: OAuth2PasswordBearer

    def __init__(self, token_url: str):
        self.scheme = OAuth2PasswordBearer(tokenUrl=token_url)


class Constants(object):
    authorization: Authorization
    lengths: dict = dict(strings=[64, 128, 256])

    def __init__(self, base_url: str = "http://localhost:8000/"):
        self.authorization = Authorization(f"{base_url}/api/oauth/token")
