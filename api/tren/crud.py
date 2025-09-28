from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Tren


async def create_tren(session:AsyncSession,group:str,exercise:str,cardio:float,user_id):
    new_tren = Tren(user_id=user_id,body_group=group,exercise=exercise,cardio=cardio)
    session.add(new_tren)
    await session.commit()
    return new_tren

async def get_all_trens(session:AsyncSession,user_id:int)