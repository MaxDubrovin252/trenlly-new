from pydantic import BaseModel

class Profile(BaseModel):
    first_name:str |None = None
    last_name:str | None = None
    weight:float
    height:float
    