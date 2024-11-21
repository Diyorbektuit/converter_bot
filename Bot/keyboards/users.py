from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def home_reply_keyboard() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="🗣Referall link olish")
    button_2 = KeyboardButton(text="Taklif yuborish")
    button_3 = KeyboardButton(text="Fayllarni turini o'zgartirish")
    button_4 = KeyboardButton(text="🗂Xizmatlar")
    button_5 = KeyboardButton(text="💰Mening hisobim")
    button_6 = KeyboardButton(text="🔄Fayllarni arxivlash va arxivdan chiqarish")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_3],
            [button_6],
            [button_4],
            [button_2]
        ],
        resize_keyboard=True
    )
    return reply

def home_reply_keyboard_admin() -> ReplyKeyboardMarkup:
    button_2 = KeyboardButton(text="userlar ma'lumoti")
    button_3 = KeyboardButton(text="hamma userlarga xabar jo'natish")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_3],
            [button_2]
        ],
        resize_keyboard=True
    )
    return reply

def convert_reply_keyboard() -> ReplyKeyboardMarkup:
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

def archive_keyboard() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="zip ko'rinishida arxivlash")
    button_2 = KeyboardButton(text="rar ko'rinishda arxivlash")
    button_4 = KeyboardButton(text="zip arxivdan chiqarish")
    button_5 = KeyboardButton(text="rar arxivdan chiqarish")
    button_3 = KeyboardButton(text="⬅️Orqaga")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_1, button_2],
            [button_4, button_5],
            [button_3]
        ],
        resize_keyboard=True
    )
    return reply

def archive_finish() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="yakunlash")
    button_2 = KeyboardButton(text="Asosiy sahifa")
    button_3 = KeyboardButton(text="⬅️Orqaga")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_1],
            [button_3],
            [button_2]
        ],
        resize_keyboard=True
    )
    return reply