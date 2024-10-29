from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def offer_reply_keyboard():
    button_3 = KeyboardButton(text="⬅️Orqaga")

    reply = ReplyKeyboardMarkup(
        keyboard=[
            [button_3]
        ],
        resize_keyboard=True
    )
    return reply