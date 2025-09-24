import jwt
from datetime import datetime, timedelta
from core import settings

def create_access_token(username:str,user_id:int,exp_time=1)->str:
    payload = {
        "sub":username,
        "iat":datetime.utcnow(),
        "exp":datetime.utcnow()+timedelta(hours=exp_time),
        "user_id":user_id
    }
    
    token = jwt.encode(payload, settings.jwt.secret_key,settings.jwt.algorithm)
    return token
    
def validate_token(token:str):
    try:
        decode = jwt.decode(token,settings.jwt.secret_key,algorithms=[settings.jwt.algorithm])
        return decode
    except jwt.InvalidTokenError:
        return False
    except jwt.ExpiredSignatureError:
        return None