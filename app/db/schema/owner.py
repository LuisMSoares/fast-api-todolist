from pydantic import BaseModel
from typing import List, Dict, Union, Optional
from .todo import Todo

class OwnerBase(BaseModel):
    title: str
    owner: str

class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: int
    todo: List[Todo] = []

    class Config:
        orm_mode = True
