from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
load_dotenv()
import os
CHANNEL = os.getenv('CHANNEL')

def channels_buttons() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Telegram Kanalimiz", url=f'https://t.me/{CHANNEL}')
    keyboard.button(text="Tekshirish", callback_data="check")

    return keyboard.as_markup()