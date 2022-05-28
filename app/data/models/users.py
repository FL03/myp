from pydantic import BaseModel


class User(BaseModel):
    key: str
    ensname: str
    email: str
    created_at: str


class UserIn(User):
    hashed_password: str
