from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from typing import List
from app.db import schema, get_db
from app.crud.todo import create_todo, get_all_todo_by_owner, get_one_todo_by_id


todo_router = APIRouter()


@todo_router.get('/{owner_name}', response_model=List[schema.Todo])
def get_all_todo_by_owner_route(owner_name: str, db: Session = Depends(get_db)):
    return get_all_todo_by_owner(db, owner_name)

@todo_router.get('/{owner_name}/{todo_id}', response_model=schema.Todo)
def get_one_todo_by_id_route(owner_name: str, todo_id: int, db: Session = Depends(get_db)):
    return get_one_todo_by_id(db, owner_name, todo_id)

@todo_router.post('/{owner_name}/', response_model=schema.Todo, status_code=201)
def create_todo_route(owner_name: str, todo_data: schema.TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, owner_name, todo_data)


