# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os

# # Получаем URL базы данных из переменной окружения или задаем вручную
# DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://todo_user:your_password@localhost/todo_db')

# # Создаем движок SQLAlchemy
# engine = create_engine(DATABASE_URL)

# # Создаем фабрику сессий
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Создаем базовый класс для моделей
# Base = declarative_base()
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://todo_user:your_password@localhost/todo_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
