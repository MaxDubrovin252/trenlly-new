from sqlalchemy.orm import mapped_column,Mapped, declared_attr, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    
    
class UserRelalationMixin:
    _user_id_nullable_:bool=False
    _user_id_unique_:bool = False
    _user_back_populates_:str | None = None
    
    
    @declared_attr
    def user_id(cls)->Mapped[int]:
        return mapped_column(ForeignKey("users.id"),unique=cls._user_id_unique_,nullable=cls._user_id_nullable_)
    
    @declared_attr
    def user(cls)->Mapped[User]:
        return relationship("User", back_populates=cls._user_back_populates_)
    