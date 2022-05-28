from typing import List

from fastapi import APIRouter

from app.core.session import session
from app.data.models import items

db = session.deta.Base("items")
router: APIRouter = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def fetch_users_items(query) -> List[dict]:
    return db.fetch(query=query).items


@router.get("/{cid}")
async def get_item_by_key(cid: str):
    return db.get(key=cid)


@router.post("/add")
async def add_item(item: items.Item):
    return db.put(data=items.ItemIn(**item.dict()).dict())
