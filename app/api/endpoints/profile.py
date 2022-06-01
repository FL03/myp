from fastapi import APIRouter

from app.core.session import session

db = session.deta.Base("profile")
router: APIRouter = APIRouter(prefix="/profile", tags=["profile"])


@router.get("/")
async def load_profile(query=None):
    return db.fetch(query=query).items


@router.get("/settings")
async def profile_settings():
    return db.fetch()
