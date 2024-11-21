from aiogram import Bot, Dispatcher
from dotenv import load_dotenv



import os
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
CHANNEL = os.getenv('CHANNEL')
ADMIN = os.getenv('ADMIN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

async def check_member(telegram_id: int) -> bool:
    chat_username = f"@{CHANNEL}"
    try:
        member = await bot.get_chat_member(chat_username, telegram_id)
        status = member.status
        a = status in ('member', 'creator', 'administrator')
        if not a:
            return False
        return True
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return False
