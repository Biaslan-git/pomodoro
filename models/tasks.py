from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    pomodoro_count: Mapped[str]
    category_id: Mapped[int]
    
class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[Optional[str]]
    name: Mapped[str]

