from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"