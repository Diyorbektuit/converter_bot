import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramRetryAfter, TelegramBadRequest
from Bot.middeware.check_member import ChannelSubscriptionMiddleware
from Database.Tables import User
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL = os.getenv('CHANNEL')
ADMIN = os.getenv('ADMIN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

dp.message.middleware(ChannelSubscriptionMiddleware("@foydali_tgbotlar", bot))

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
