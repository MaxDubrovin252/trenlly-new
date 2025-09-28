from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .profile import Profile
    from .tren import Tren

class User(Base):
    username:Mapped[str] = mapped_column(unique=True)
    password:Mapped[bytes] 
    
    profile:Mapped["Profile"] = relationship("Profile",back_populates="user")
    trens:Mapped[list["Tren"]] = relationship("Tren",back_populates="user")