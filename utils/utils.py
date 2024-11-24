from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import asyncio
from aiogram import Bot
from aiogram.exceptions import TelegramRetryAfter, TelegramBadRequest
from Database.Tables import User
from Bot.middeware.check_member import SubscriptionMiddleware
import os
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL = os.getenv('CHANNEL')
ADMIN = os.getenv('ADMIN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
dp.update.middleware(SubscriptionMiddleware([CHANNEL]))

async def send_message_to_all_users(bot_: Bot, text: str) -> dict:
    users = await User.all_users()
    users_count = len(list(users))
    count = 0
    for user in users:
        try:
            await bot_.send_message(chat_id=user.telegram_id, text=text)
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
