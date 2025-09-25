from service.utils import validate_token
from fastapi import HTTPException

def user_verify_by_token(token:str):
    correct = validate_token(token)

    if correct is False:
        raise HTTPException(status_code=401, detail="invalid credentials")
    if correct is None:
        raise HTTPException(status_code=401,detail="period of life has been expired")
    return correct