# from fastapi import FastAPI
# from app.database import engine, Base
# from app.routes import auth, tasks  # Явные пути к модулям

# # Создание таблиц в базе данных
# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Подключение маршрутов
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, tasks

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Создание приложения FastAPI
app = FastAPI()

# Подключение маршрутов
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

