from fastapi import APIRouter, Depends

from app.api.endpoints import auth, components, ethereum, items, profile, users
from app.utils.users import get_current_active_user

router: APIRouter = APIRouter(prefix="/api", tags=["default"])
router.include_router(router=auth.router)
router.include_router(router=components.router, dependencies=[Depends(get_current_active_user)])
router.include_router(router=ethereum.router, dependencies=[Depends(get_current_active_user)])
router.include_router(router=items.router, dependencies=[Depends(get_current_active_user)])
router.include_router(router=profile.router, dependencies=[Depends(get_current_active_user)])
router.include_router(router=users.router)
