from fastapi import APIRouter
from app.api_v1.referrers.views import router as referrers_router

router = APIRouter()
router.include_router(router=referrers_router, prefix="/referrers")
