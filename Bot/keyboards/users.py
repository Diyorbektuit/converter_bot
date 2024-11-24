from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def home_reply_keyboard() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="🔗 Referal havolani olish")
    button_2 = KeyboardButton(text="✉️ Taklif va fikr bildirish")
    button_3 = KeyboardButton(text="📂 Fayl turini o'zgartirish")
    button_4 = KeyboardButton(text="🔧 Xizmatlar ro'yxati")
    button_5 = KeyboardButton(text="💰 Hisobingizni tekshirish")
    button_6 = KeyboardButton(text="📦 Fayllarni arxivlash yoki arxivdan chiqarish")

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
    button_1 = KeyboardButton(text="👥 Foydalanuvchilar haqida ma'lumot")
    button_2 = KeyboardButton(text="📨 Hamma foydalanuvchilarga xabar yuborish")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_2],
            [button_1]
        ],
        resize_keyboard=True
    )
    return reply

def convert_reply_keyboard() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="📄 Faylni PDF formatiga o'zgartirish")
    button_2 = KeyboardButton(text="📊 Faylni PPTX formatiga o'zgartirish")
    button_3 = KeyboardButton(text="📃 Faylni DOCX formatiga o'zgartirish")
    button_4 = KeyboardButton(text="🏠 Asosiy sahifaga qaytish")

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
    button_1 = KeyboardButton(text="📦 ZIP formatida arxivlash")
    button_2 = KeyboardButton(text="📦 RAR formatida arxivlash")
    button_3 = KeyboardButton(text="📂 ZIP arxivdan chiqarish")
    button_4 = KeyboardButton(text="📂 RAR arxivdan chiqarish")
    button_5 = KeyboardButton(text="🏠 Asosiy sahifaga qaytish")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_1, button_2],
            [button_3, button_4],
            [button_5]
        ],
        resize_keyboard=True
    )
    return reply

def archive_finish() -> ReplyKeyboardMarkup:
    button_1 = KeyboardButton(text="✅ Arxivlashni yakunlash")
    button_2 = KeyboardButton(text="🏠 Asosiy sahifaga qaytish")
    button_3 = KeyboardButton(text="⬅️ Orqaga qaytish")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_1],
            [button_3],
            [button_2]
        ],
        resize_keyboard=True
    )
    return reply
