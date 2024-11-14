import os

from dotenv import load_dotenv

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ID администратора
ADMIN_TG_ID = os.getenv('ADMIN_TG_ID')

# Данные для подключения к базе данных
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')

INVITE_LINK = os.getenv('INVITE_LINK')
DEBUG = bool(os.getenv('DEBUG'))
