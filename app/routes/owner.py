from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from typing import List
from app.db import schema, get_db
from app.crud.owner import create_owner, get_all_owners, update_owner, get_one_owner_by_id


owner_router = APIRouter()


@owner_router.get('/', response_model=List[schema.Owner])
def get_all_owners_route(db: Session = Depends(get_db)):
    return get_all_owners(db)

@owner_router.get('/{owner_id}', response_model=schema.Owner)
def get_one_owner_by_id_route(owner_id: int, db: Session = Depends(get_db)):
    return get_one_owner_by_id(db, owner_id)

@owner_router.post('/', response_model=schema.Owner, status_code=201)
def create_owner_route(owner_data: schema.OwnerCreate, db: Session = Depends(get_db)):
    return create_owner(db, owner_data)

@owner_router.put('/{owner_id}', response_model=schema.Owner, status_code=201)
def update_owner_route(owner_id: int, owner_data: schema.OwnerCreate, db: Session = Depends(get_db)):
    return update_owner(db, owner_id, owner_data)