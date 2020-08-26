from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class OwnerModel(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    owner = Column(String, nullable=False, unique=True)

    todo = relationship("TodoModel", back_populates="owner_todo")


class TodoModel(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner_todo = relationship("OwnerModel", back_populates="todo")
    todo_tag = relationship("TodoTagModel", back_populates="todo")


class TodoTagModel(Base):
    __tablename__ = 'todos_tags'

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, nullable=False)
    todo_id = Column(Integer, ForeignKey("todos.id"))

    todo = relationship("TodoModel", back_populates="todo_tag")