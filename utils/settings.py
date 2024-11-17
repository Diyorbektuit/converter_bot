import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL = os.getenv('CHANNEL')
ADMIN = os.getenv('ADMIN')
DATABASE_URL = os.getenv('DATABASE_URL')
ECHO = os.getenv('ECHO')
POINT = os.getenv('POINT')

class Settings:
    API_TOKEN: str = API_TOKEN
    CHANNEL : str = CHANNEL
    ADMIN : int = ADMIN
    DATABASE_URL : str = DATABASE_URL
    ECHO : bool = ECHO
    POINT: int = POINT


SETTINGS = Settings()

