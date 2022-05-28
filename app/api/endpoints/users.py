from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.core.session import session
from app.data.models.users import User, UserIn
from app.utils.messages import Status
from app.utils.users import get_current_active_user, get_password_hash

db = session.deta.Base("users")
router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List)
async def get_users():
    return db.fetch().items


@router.post("/new")
async def create_user(ensname: str, password: str):
    return db.put(UserIn(ensname=ensname, hashed_password=get_password_hash(password)).dict())


@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/user/{user_key}", response_model=User)
async def get_user(user_key: str):
    return await db.get(user_key)


@router.put("/user/{user_key}", response_model=User)
async def update_user(user_key: str, user: UserIn):
    await db.update(key=user_key, updates=user.dict(exclude_unset=True))
    return await get_user(user_key)


@router.delete("/user/{user_key}", response_model=Status)
async def delete_user(user_key: str):
    deleted_count = db.delete(user_key)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_key} not found")
    return Status(message=f"Deleted user {user_key}")
