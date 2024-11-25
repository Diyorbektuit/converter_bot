from aiogram import BaseMiddleware, types
from Bot.keyboards.channels import channels_buttons

class ChannelSubscriptionMiddleware(BaseMiddleware):
    def __init__(self, channel, bot):
        self.channel = channel
        self.bot = bot

    async def __call__(self, handler, event, data):
        if isinstance(event, types.Message):
            message = event
            member = await self.bot.get_chat_member(self.channel, message.from_user.id)
            if member.status not in ['member', 'administrator', 'creator']:
                return await message.answer(
                    "Bizning kanallarimizga obuna boling keyin botda to'laqonli foydalana olasiz🙃",
                    reply_markup=channels_buttons()
                )
        return await handler(event, data)
