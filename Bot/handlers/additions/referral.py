from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.settings import SETTINGS
from Database.Tables import User
from Bot.keyboards import users
import uuid

router = Router()

@router.message(lambda message: message.text == "🗣Referall link olish")
async def offer_first(message: Message, state: FSMContext):
    # Foydalanuvchini ma'lumotlar bazasidan olish
    user = await User.get(telegram_id=message.from_user.id)

    if user.referral is not None:
        # Foydalanuvchida allaqachon referal link mavjud bo'lsa
        return await message.answer(
            text=(
                "📢 Sizning referal linkingiz tayyor:\n\n"
                f"🔗 https://t.me/{SETTINGS.BOT_URL}/?start={user.referral}\n\n"
                "📲 Ushbu havolani do‘stlaringizga yuboring va bonuslar oling! 🎉"
            ),
            reply_markup=users.home_reply_keyboard()
        )
    else:
        # Yangi referal link yaratish
        new_referral = str(uuid.uuid4())
        await user.update(referral=new_referral)

        await state.clear()
        await message.answer(
            text=(
                "✅ Sizga maxsus referal link yaratildi:\n\n"
                f"🔗 https://t.me/converter_uzbbot/?start={new_referral}\n\n"
                "📢 Ushbu havolani do‘stlaringizga ulashing va sovg‘alarni qo‘lga kiriting! 🎁"
            ),
            reply_markup=users.home_reply_keyboard()
        )
