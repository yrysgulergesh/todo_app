# from sqlalchemy.orm import Session
# from . import models, schemas
# from passlib.context import CryptContext

# # Создание контекста для хэширования паролей
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = get_password_hash(user.password)
#     db_user = models.User(username=user.username, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()

# def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
#     db_task = models.Task(**task.dict(), owner_id=user_id)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     return db_task

# def get_tasks(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Task).offset(skip).limit(limit).all()

# def get_task(db: Session, task_id: int):
#     return db.query(models.Task).filter(models.Task.id == task_id).first()

# def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
#     db_task = get_task(db, task_id)
#     if db_task:
#         for key, value in task.dict().items():
#             setattr(db_task, key, value)
#         db.commit()
#         db.refresh(db_task)
#     return db_task

# def delete_task(db: Session, task_id: int):
#     db_task = get_task(db, task_id)
#     if db_task:
#         db.delete(db_task)
#         db.commit()
#         return True
#     return False

# app/crud.py
'''
from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # Здесь нужно использовать bcrypt или другую библиотеку для хеширования
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task: schemas.TaskUpdate, task_id: int):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    for var, value in vars(task).items():
        setattr(db_task, var, value) if value else None

    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).offset(skip).limit(limit).all()
'''
# app/crud.py

# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# You can add additional CRUD operations here...

