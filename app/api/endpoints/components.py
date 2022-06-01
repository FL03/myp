from fastapi import APIRouter

from app.core.session import session
from app.data.models.components import Component, ComponentStore
from app.utils.messages import Status

db = session.deta.Base("components")
router: APIRouter = APIRouter(prefix="/components", tags=["components"])


@router.get("/")
async def components(query=None):
    return db.fetch(query=query).items


@router.post("/", response_model=ComponentStore)
async def component_create(component: Component):
    format_for_db = ComponentStore(**component.dict())
    db.put(data=format_for_db.dict(), key=format_for_db.key)
    return db.get(key=format_for_db.key)


@router.get("/{key}")
async def component_get(key: str):
    return db.get(key)


@router.delete("/{key}")
async def component_delete(key: str):
    for i in db.fetch().items:
        if key == i["key"]:
            db.delete(key)
            break
        else:
            raise (LookupError, "Could not find a {}(key={})".format("Component", key))
    return Status(message=f"Deleted user {key}")


@router.put("/{key}")
async def component_update(key: str, component: Component = None):
    db.update(key, updates=component.dict())
    return ComponentStore(**db.get(key))
