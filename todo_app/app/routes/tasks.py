
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from app.auth import get_current_user  # Импорт функции

router = APIRouter()

@router.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(SessionLocal),
    current_user: schemas.User = Depends(get_current_user)
):
    tasks = crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
    return tasks

