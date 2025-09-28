from fastapi import APIRouter, Depends,HTTPException, Form
from api.user.dependencies import user_verify_by_token
from .schemas import Tren
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud



router = APIRouter(prefix="/trens", tags=["treny"])

@router.post("/create")
async def create_tren(
    correct:str = Depends(user_verify_by_token),
    tren:Tren = Form(),
    session:AsyncSession = Depends(db_helper.session_dependency)
    ):
    id = correct["user_id"]
    
    new_tren = await crud.create_tren(
        session=session,
        group=tren.group,
        exercise=tren.exercise,
        cardio=tren.cardio,
        user_id=id,
    )
    return {"new tren created":new_tren}
    