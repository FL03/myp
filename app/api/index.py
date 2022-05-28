from fastapi import APIRouter

from app.api.endpoints import auth, ethereum, items, users

router: APIRouter = APIRouter(prefix="/api", tags=["default"])
router.include_router(router=auth.router)
router.include_router(router=ethereum.router)
router.include_router(router=items.router)
router.include_router(router=users.router)
