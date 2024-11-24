from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Bot.states.user import Offer
from utils.utils import bot, ADMIN
from Database.Tables import UserOffer, User
from Bot.keyboards import users

router = Router()

@router.message(Offer.message, lambda message: message.voice or None)
async def audio_offer(message: Message, state: FSMContext):
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    user = await User.get(
        telegram_id=message.from_user.id
    )

    if user is not None:
         await UserOffer.create(
            user=user,
            file=message.voice.file_id
        )

    response = (
        "📥 *Yangi taklif keldi:*\n\n"
        f"👤 *Foydalanuvchi:* {message.from_user.full_name}\n"
        f"🆔 *Telegram ID:* {message.chat.id}\n"
        f"📅 *Xabar kelgan sana:* {message.date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"🔗 *Username:* @{message.from_user.username or 'No username'}"
    )

    await message.reply(
        "✅ *Taklifingiz qabul qilindi!*\nTaklifingiz uchun rahmat 😊",
        reply_markup=users.home_reply_keyboard(),
        parse_mode="Markdown",
    )

    await state.clear()
    await bot.send_voice(chat_id=int(ADMIN), voice=message.voice.file_id, caption=response)

@router.message(Offer.message, lambda message: message.text or None)
async def text_offer(message: Message, state: FSMContext):
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    user = await User.get(
        telegram_id=message.from_user.id
    )

    if user is not None:
        await UserOffer.create(
            user=user,
            text=message.text
        )

    response = (
        "📥 *Yangi taklif keldi:*\n\n"
        f"👤 *Foydalanuvchi:* {message.from_user.full_name}\n"
        f"🆔 *Telegram ID:* {message.chat.id}\n"
        f"📅 *Xabar kelgan sana:* {message.date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"🔗 *Username:* @{message.from_user.username or 'No username'}\n\n"
        f"📝 *Taklif matni:* {message.text}"
    )

    await message.reply(
        "✅ *Taklifingiz qabul qilindi!*\nTaklifingiz uchun rahmat 😊",
        reply_markup=users.home_reply_keyboard(),
        parse_mode="Markdown",
    )

    await state.clear()
    await bot.send_message(chat_id=int(ADMIN), text=response)
