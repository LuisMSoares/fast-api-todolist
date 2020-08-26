from sqlalchemy.orm import Session
from typing import List
from app.db import models, schema


def get_all_owners(db: Session) -> List[schema.Owner]:
    return db.query(models.OwnerModel).all()

def get_all_owners_by_owner_name(db: Session, owner_name: str) -> List[schema.Owner]:
    return db.query(models.OwnerModel).filter(models.OwnerModel.owner == owner_name).all()

def get_one_owner_by_id(db: Session, id: int) -> schema.Owner:
    return db.query(models.OwnerModel).filter(models.OwnerModel.id == id).first()

def create_owner(db: Session, owner_data: schema.OwnerCreate) -> schema.Owner:
    db_owner = models.OwnerModel(
        title = owner_data.title,
        owner = owner_data.owner
    )
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def update_owner(db: Session, owner_id: int, owner_data: schema.OwnerCreate) -> schema.Owner:
    db_owner = get_one_owner_by_id(db, owner_id)
    if db_owner:
        db_owner.title = owner_data.title
        db_owner.owner = owner_data.owner
    db.commit()
    db.refresh(db_owner)
    return db_owner
