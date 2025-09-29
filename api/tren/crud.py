from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Tren


async def create_tren(session:AsyncSession,group:str,exercise:str,cardio:float,user_id):
    new_tren = Tren(user_id=user_id,body_group=group,exercise=exercise,cardio=cardio)
    session.add(new_tren)
    await session.commit()
    return new_tren

async def get_all_trens(session:AsyncSession,user_id:int):
    stmt = select(Tren).where(Tren.user_id==user_id)
    res = await session.execute(statement=stmt)
    trens = res.scalars().all()
    return list(trens)


    
