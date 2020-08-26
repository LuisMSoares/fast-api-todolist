from pydantic import BaseModel
from typing import List, Dict, Union, Optional
from .todo_tag import TodoTag


class TodoBase(BaseModel):
    title: str
    content: str

class TodoCreate(TodoBase):
    tags: List[str] = []

class Todo(TodoBase):
    id: int
    todo_tag: List[TodoTag] = []

    class Config:
        orm_mode = True
