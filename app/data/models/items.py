from pydantic import BaseModel


class Item(BaseModel):
    category: str
    content: str
