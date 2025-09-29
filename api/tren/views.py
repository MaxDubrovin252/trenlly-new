from fastapi import APIRouter, Depends,HTTPException, Form
from api.user.dependencies import user_verify_by_token
from .schemas import Tren
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud, service



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
        cardio=tren.cardio_hours,
        user_id=id,
    )
    return {"new tren created":new_tren}
    
    
@router.get("/all")
async def get_all(
    session:AsyncSession = Depends(db_helper.session_dependency),
    correct:str = Depends(user_verify_by_token)
):
    user_id = correct["user_id"]
    trens = await crud.get_all_trens(session=session, user_id=user_id)
    return {"all your trens":trens}

@router.get("/statistic/cardio")
async def get_cardio(
    session:AsyncSession = Depends(db_helper.session_dependency),
    correct:str = Depends(user_verify_by_token),
):
    user_id = correct["user_id"]
    trens = await crud.get_all_trens(session=session, user_id=user_id)
    message = service.average_cardio(trens=trens)
    return message 

@router.get("/statistic/main-group")
async def get_main_group(
    session:AsyncSession = Depends(db_helper.session_dependency),
    correct:str = Depends(user_verify_by_token),
):
    user_id = correct["user_id"]
    trens = await crud.get_all_trens(session=session, user_id=user_id)
    message = service.groups(trens=trens)
    return message 


@router.get("/statistic/main-exercise")
async def get_main_group(
    session:AsyncSession = Depends(db_helper.session_dependency),
    correct:str = Depends(user_verify_by_token),
):
    user_id = correct["user_id"]
    trens = await crud.get_all_trens(session=session, user_id=user_id)
    message = service.exercise_freq(trens=trens)
    return message 
