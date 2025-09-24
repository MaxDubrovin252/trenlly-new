from service.utils import hash_password, verify_password, create_access_token
from repository import user
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(session:AsyncSession, username:str, password:str):
    hash_pass = hash_password(password=password)
    new_user = await user.create_user(session=session,username=username, hash_pass=hash_pass)
    return new_user

async def verify_user(session:AsyncSession,username:str,password:str):
    user_in = await user.get_user_by_username(session=session,username=username)
    
    
    is_valid = verify_password(password=password,hash_pass=user_in.password)
    
    if is_valid is False:
        return None
    
    token = create_access_token(username=username,user_id=user_in.id)
    
    return token