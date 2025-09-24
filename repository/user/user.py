from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select

async def get_user_by_username(session:AsyncSession,username:str)->User|None:
    stmt = select(User).where(User.username==username)
    res = await session.execute(statement=stmt)
    user = res.scalars().one_or_none()
    return user


async def create_user(session:AsyncSession, username:str, hash_pass:bytes)->User|None:
    user_exist = await get_user_by_username(session=session, username=username)
    if user_exist:
        await session.rollback()
        return None
    
    new_user = User(username=username,password=hash_pass)
    session.add(new_user)
    await session.commit()
    return new_user
    
        