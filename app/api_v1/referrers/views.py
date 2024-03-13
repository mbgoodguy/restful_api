from fastapi import APIRouter, Depends
from . import crud
from .schemas import Referrer, ReferrerCreate
from ...core.models import db_helper

router = APIRouter(tags=["Referrers"])


@router.post("/create", response_model=Referrer)
async def create_referrer(
    referrer_in: ReferrerCreate,
    session=Depends(),
):
    return await crud.create_referrer(session=session, referrer_in=referrer_in)
