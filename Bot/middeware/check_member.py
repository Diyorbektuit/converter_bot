from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums import ChatMemberStatus


class SubscriptionMiddleware(BaseMiddleware):
    def __init__(self, required_channels: list):
        """
        Middleware obuna tekshiruvi uchun.
        :param required_channels: Kanal username'lari ro'yxati, masalan ["@kanal1", "@kanal2"]
        """
        self.required_channels = required_channels
        super().__init__()

    async def check_subscription(self, bot, user_id: int, channel: str) -> bool:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            return member.status in {ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR}
        except TelegramBadRequest:
            return False

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            user_id = event.from_user.id
            bot = data["bot"]

            for channel in self.required_channels:
                is_subscribed = await self.check_subscription(bot, user_id, channel)
                if not is_subscribed:
                    await event.reply(f"❌ Siz {channel} kanaliga obuna bo'lmagansiz! Iltimos, avval obuna bo'ling.")
                    return

        return await handler(event, data)
