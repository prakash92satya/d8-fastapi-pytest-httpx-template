from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Task

router = APIRouter(prefix="/tasks")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_task(title: str, db: Session = Depends(get_db)):
    task = Task(title=title, owner_id=1)
    db.add(task)
    db.commit()
    return {"msg": "task created"}

@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()