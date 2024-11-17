from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def home_reply_keyboard():
    button_1 = KeyboardButton(text="🗣Referall link olish")
    button_2 = KeyboardButton(text="Taklif yuborish")
    button_3 = KeyboardButton(text="Fayllarni turini o'zgartirish")
    button_4 = KeyboardButton(text="🗂Xizmatlar")
    button_5 = KeyboardButton(text="💰Mening hisobim")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_4, button_5],
            [button_2, button_1],
            [button_3]
        ],
        resize_keyboard=True
    )
    return reply


def convert_reply_keyboard():
    button_1 = KeyboardButton(text="pdf ga aylantirish")
    button_2 = KeyboardButton(text="pptx ga aylantirish")
    button_3 = KeyboardButton(text="docx ga aylantirish")
    button_4 = KeyboardButton(text="⬅️Orqaga")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_1, button_2],
            [button_3],
            [button_4]
        ],
        resize_keyboard=True
    )
    return reply