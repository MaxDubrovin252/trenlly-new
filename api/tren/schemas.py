from pydantic import BaseModel

class Tren(BaseModel):
    group:str
    exercise:str
    cardio_hours:float
    