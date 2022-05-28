from typing import List

from fastapi import APIRouter, HTTPException

from app.core.session import session
from app.data.models.users import User, UserIn
from app.utils.messages import Status

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


async def get_user(user_key: str):
    return session.db.get(user_key)


@router.get("/", response_model=List)
async def get_users():
    return session.db.fetch().items


@router.post("/new", response_model=User)
async def create_user(user: UserIn):
    user.hashed_password = session.constants.authorization.context.hash(user.hashed_password)
    return session.db.put(user)


@router.get("/user/{user_key}", response_model=User)
async def get_user(user_key: str):
    return await session.db.get(user_key)


@router.put("/user/{user_key}", response_model=User)
async def update_user(user_key: str, user: UserIn):
    await session.db.update(key=user_key, updates=user.dict(exclude_unset=True))
    return await get_user(user_key)


@router.delete("/user/{user_key}", response_model=Status)
async def delete_user(user_key: str):
    deleted_count = session.db.delete(user_key)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_key} not found")
    return Status(message=f"Deleted user {user_key}")
