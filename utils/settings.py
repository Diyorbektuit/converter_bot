import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL = os.getenv('CHANNEL')
ADMIN = os.getenv('ADMIN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
ECHO = os.getenv('ECHO')

class Settings:
    API_TOKEN: str = API_TOKEN
    CHANNEL : str = CHANNEL
    ADMIN : int = ADMIN
    DATABASE_URL : str = DATABASE_URL
    ECHO : bool = ECHO


SETTINGS = Settings()

