from fastapi import APIRouter, Depends
from . import crud
from .schemas import Referrer, ReferrerCreate
from ...core.database import get_db

router = APIRouter(tags=["Referrers"])


@router.post("/create", response_model=Referrer)
async def create_referrer(
    referrer_in: ReferrerCreate,
    session=Depends(get_db),
):
    return await crud.create_referrer(session=session, referrer_in=referrer_in)
