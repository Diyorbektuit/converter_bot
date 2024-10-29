import asyncio
from Database.Tables import User

async def fetch_user():
    user = await User.get(telegram_id=1651596533)
    print(user.username)

# Run the async function
asyncio.run(fetch_user())