from typing import Optional
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeMeta, Mapped, declarative_base, mapped_column


Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    pomodoro_count: Mapped[str]
    category_id: Mapped[int]
    
class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[Optional[str]]
    name: Mapped[str]

