from fastapi import APIRouter, Depends

from app.core.session import session
from app.data.models.users import User, UserIn
from app.utils.messages import Status
from app.utils.users import get_current_active_user, get_password_hash

db = session.deta.Base("users")
router: APIRouter = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def load_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/")
async def create_user(username: str, password: str):
    return db.put(UserIn(username=username, hashed_password=get_password_hash(password)).dict())


@router.put("/", dependencies=[Depends(get_current_active_user)], response_model=UserIn)
async def update_current_user(current_user: UserIn = Depends(get_current_active_user), updates: UserIn = None):
    db.update(key=current_user.key, updates=dict(current_user, **updates.dict(exclude_unset=True)))
    return UserIn(**db.get(current_user.key))


@router.delete("/", response_model=Status)
async def delete_user(key: str):
    for i in db.fetch().items:
        if key == i["key"]:
            db.delete(key)
            break
        else:
            raise (LookupError, "Failed to delete User(key={})".format(key))
    return Status(message=f"Deleted user {key}")
