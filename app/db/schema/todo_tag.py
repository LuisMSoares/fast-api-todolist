from pydantic import BaseModel
from typing import List, Dict, Union, Optional


class TodoTagBase(BaseModel):
    todo_id: int
    tag: str

class TodoTagCreate(TodoTagBase):
    pass

class TodoTag(TodoTagBase):
    id: int

    class Config:
        orm_mode = True