from .base import Base
from sqlalchemy import ForeignKey,func, DateTime
from sqlalchemy.orm import Mapped,mapped_column, relationship
from .mixins import UserRelalationMixin
from datetime import datetime




class Tren(UserRelalationMixin,Base):
    _user_back_populates_ = "trens"
    
    body_group:Mapped[str]
    exercise:Mapped[str]
    cardio:Mapped[float]
    
    
    def __str__(self):
        return f"tren:{self.group}"