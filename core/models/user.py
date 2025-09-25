from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .profile import Profile


class User(Base):
    username:Mapped[str] = mapped_column(unique=True)
    password:Mapped[bytes] 
    
    profile:Mapped["Profile"] = relationship(back_populates="user")