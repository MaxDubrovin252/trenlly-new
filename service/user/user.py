from service.utils import hash_password
from repository import user
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(session:AsyncSession, username:str, password:str):
    hash_pass = hash_password(password=password)
    new_user = await user.create_user(session=session,username=username, hash_pass=hash_pass)
    return new_user
