from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def service_buttons() -> InlineKeyboardMarkup:
    button_1 = InlineKeyboardButton(text="Fayl turini o'zgartirish", callback_data="converter")
    button_2 = InlineKeyboardButton(text="Boshqa xizmatlar", callback_data="other")
    button_3 = InlineKeyboardButton(text="Fayllarni arxivlash va arxivdan chiqarish", callback_data="archive")

    reply = InlineKeyboardMarkup(inline_keyboard=[
        [button_1],
        [button_3],
        [button_2],
    ])

    return reply


def rar_buttons() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="fayyalarni rar turida arxivlash", callback_data="convert_rar")
    keyboard.button(text="zar arxividan chiqarish", callback_data="rar_to_files")

    return keyboard.as_markup()