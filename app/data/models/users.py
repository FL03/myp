from pydantic import BaseModel


class User(BaseModel):
    ensname: str
    email: str | None = None
    disabled: bool | None = None


class UserIn(User):
    hashed_password: str
