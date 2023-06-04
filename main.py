from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import FastAPI, Depends
import models
from database import engine,SessionLocal
from models import Todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoRequest(BaseModel):
    title: str
    description: str
    priority: int
    complete: bool





@app.get("/main")
async def read_all(db: Annotated[Session,Depends(get_db)]):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}")
async def read_todo(db: Annotated[Session,Depends(get_db)] ,todo_id:int):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
@app.post("/todo/{todo_id}")
async def read_todo(db: Annotated[Session,Depends(get_db)] ,todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()