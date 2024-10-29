from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.utils import CHANNEL


def channels_buttons() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Telegram Kanalimiz", url=f'https://t.me/{CHANNEL}')
    keyboard.button(text="Tekshirish", callback_data="check")

    return keyboard.as_markup()