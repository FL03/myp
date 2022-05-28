from pydantic import BaseModel


class Constants(BaseModel):
    lengths: dict = dict(strings=[64, 128, 256])
