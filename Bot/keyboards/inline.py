from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def service_buttons() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Fayl turini o'zgartirish", callback_data="converter")
    keyboard.button(text="Boshqa xizmatlar", callback_data="other")

    return keyboard.as_markup()