from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class DBSettings(BaseModel):
    url:str = os.getenv("DB_URL")
    echo:bool = False
    

class JWTSettings(BaseModel):
    algorithm:str = os.getenv("ALGO")
    secret_key:str = os.getenv("SECRET_KEY")
    
    
class Settings(BaseSettings):
    db:DBSettings = DBSettings()
    jwt:JWTSettings = JWTSettings()
    
    
settigns = Settings()