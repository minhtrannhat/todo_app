from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from fastapi_todo.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    l_name = Column(String)
    f_name = Column(String)
    email = Column(String, unique=True, index=True)
    todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")
