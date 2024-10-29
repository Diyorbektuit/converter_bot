from utils.utils import dp, bot
from Bot import handlers

async def main():
    print("run the bot")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())