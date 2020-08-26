from fastapi import FastAPI
from app.db import models
from app.db.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


from .routes.owner import owner_router
app.include_router(owner_router, prefix='/owner', tags=['Owner'])
from .routes.todo import todo_router
app.include_router(todo_router, prefix='/todo', tags=['Todos'])