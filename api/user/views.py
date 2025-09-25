from fastapi import APIRouter, Depends, HTTPException
from .schemas import User
from core.models import db_helper
from service.user import create_user, verify_user
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["authorization"])

@router.post("/sign-up")
async def sign_up(user:User, session:AsyncSession = Depends(db_helper.session_dependency)):
    new_user = await create_user(session=session,username=user.username, password=user.password)
    if new_user is None:
        raise HTTPException(status_code=400, detail=f"user {user.username} already exists")
    return {"new user sign up":new_user.username}

@router.post("/sign-in")
async def sign_in(user:User, session:AsyncSession = Depends(db_helper.session_dependency)):
    token = await verify_user(session=session,username=user.username, password=user.password)
    if token is None:
        raise HTTPException(status_code=401, detail=f"password {user.password} is invalid")
    return {"token":token}


