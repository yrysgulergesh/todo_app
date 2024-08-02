import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение переменных окружения
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

# Проверка на наличие переменных окружения
if not DATABASE_URL:
    raise ValueError("Не установлена переменная окружения DATABASE_URL")

if not SECRET_KEY:
    raise ValueError("Не установлена переменная окружения SECRET_KEY")
