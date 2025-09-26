from fastapi import APIRouter,Depends,Form, HTTPException
from api.user import user_verify_by_token
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .schemas import Profile
from . import crud


router = APIRouter(prefix="/profiles", tags=["profile"])


@router.post("/")
async def create_profile(profile:Profile=Form() ,correct:str=Depends(user_verify_by_token),session:AsyncSession=Depends(db_helper.session_dependency)):
    user_id = correct["user_id"]
    
    new_profile = await crud.create_profiles(
        session=session,
        user_id=user_id,
        first_name=profile.first_name,
        last_name=profile.last_name,
        weight=profile.weight,
        height=profile.height,
        
        )
    if new_profile is None:
        raise HTTPException(status_code=400, detail=f"user {correct["sub"]} already have a profile")
    
    return {"new profile create":new_profile}


@router.get("/")
async def get_profile(correct:str=Depends(user_verify_by_token),session:AsyncSession=Depends(db_helper.session_dependency)):
    
    users = await crud.get_all(session=session)
    return users




