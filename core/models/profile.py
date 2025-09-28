from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from .mixins import UserRelalationMixin


if TYPE_CHECKING:
    from .user import User


class Profile(UserRelalationMixin,Base):
    _user_id_unique_=True
    _user_back_populates_= "profile"    
    
    
    first_name:Mapped[str|None] = None
    last_name:Mapped[str|None] = None
    weight:Mapped[float] 
    height:Mapped[float] 
    age:Mapped[int]
    
    
    def __str__(self):
        return f"first_name={self.first_name}"
    
    def __repr__(self):
        return str(self)
    
    
    
    
    
    
    
    
    