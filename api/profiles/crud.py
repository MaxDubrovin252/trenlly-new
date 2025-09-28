from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from core.models import  Profile,User
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

async def create_profiles(session:AsyncSession,
                        user_id:int,
                        
                        height:float,
                        weight:float,
                        first_name:str|None=None,
                        last_name:str|None=None):
        stmt = select(Profile).where(Profile.user_id==user_id)
        profile_exists = await session.scalar(statement=stmt)
        if profile_exists:
            await session.commit()
            return None
        
        new_profile = Profile(user_id=user_id,first_name=first_name,last_name=last_name,weight=weight,height=height)
        
        session.add(new_profile)
        await session.commit()
        return new_profile


        
        
        
async def get_all(session:AsyncSession)->list[Profile]:
    stmt = select(Profile).order_by(Profile.first_name)
    res = await session.execute(statement=stmt)
    users = res.scalars().all()
    return list(users)

async def get_user(session:AsyncSession,id:int):
    stmt = select(Profile).where(Profile.user_id==id)
    res = await session.execute(stmt)
    profile= res.scalar_one_or_none()
    return profile