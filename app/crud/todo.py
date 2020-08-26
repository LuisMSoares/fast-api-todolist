from sqlalchemy.orm import Session
from typing import List
from app.db import models, schema
from .owner import get_one_owner_by_id, get_all_owners_by_owner_name


def get_all_todo_by_owner(db: Session, owner_name: str) -> List[schema.Todo]:
    result = db.query(models.OwnerModel, models.TodoModel).outerjoin(
                models.TodoModel, models.OwnerModel.id == models.TodoModel.owner_id
              ).filter(models.OwnerModel.owner == owner_name).all()
    if not result:
        return None
    return [todo for owner,todo in result]


def get_one_todo_by_id(db: Session, owner_name: str, todo_id: int) -> schema.Todo:
    result = db.query(models.OwnerModel, models.TodoModel).outerjoin(
                models.TodoModel, models.OwnerModel.id == models.TodoModel.owner_id
              ).filter(models.TodoModel.id == todo_id).first()
    if not result:
        return None
    print(result[1])
    return result[1]

def __batch_of_todo_tag(todo_id: int, todo_tags: List[str]) -> List[schema.TodoTagCreate]:
    batch_of_todo_tag = []
    for tag in todo_tags:
        batch_of_todo_tag.append(
            models.TodoTagModel(
                tag = tag,
                todo_id = todo_id
            )
        )
    return batch_of_todo_tag

def create_todo(db: Session, owner_name: str, todo_data: schema.TodoCreate) -> schema.Todo:
    db_owner = db.query(models.OwnerModel).filter(models.OwnerModel.owner == owner_name).first()
    if not db_owner:
        return None

    db_todo = models.TodoModel(
        title = todo_data.title,
        content = todo_data.content,
        owner_id = db_owner.id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    if todo_data.tags:
        db.add_all(__batch_of_todo_tag(db_todo.id, todo_data.tags))
    db.commit()
    return get_one_todo_by_id(db, owner_name, db_todo.id)