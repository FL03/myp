import datetime

from pydantic import BaseModel


class Status(BaseModel):
    message: str


def timestamp() -> str: return str(datetime.datetime.now())
