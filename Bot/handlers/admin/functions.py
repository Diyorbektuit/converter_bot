import asyncio
from aiogram import Bot
from aiogram.exceptions import TelegramRetryAfter, TelegramBadRequest
from Database.Tables import User

async def send_message_to_all_users(bot: Bot, text: str) -> dict:
    users = await User.all_users()
    users_count = len(list(users))
    count = 0
    for user in users:
        try:
            await bot.send_message(chat_id=user.telegram_id, text=text)
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
        except TelegramBadRequest as e:
            count += 1
            if "bot was blocked by the user" in str(e):
                continue
    return {
        'success_count': users_count - count,
        'error_count': count
    }

