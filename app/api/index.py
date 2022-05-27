from fastapi import APIRouter

from .endpoints import ethereum, users

router: APIRouter = APIRouter(prefix="/api", tags=["default"])


@router.get("/auth/{ensname}")
async def authenticate(ensname: str) -> dict:
    return dict(ensname=ensname)


router.include_router(router=ethereum.router)
router.include_router(router=users.router)
