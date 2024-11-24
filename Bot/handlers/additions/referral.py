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
    user = await User.get(telegram_id=message.from_user.id)
    if user.referral is not None:
        return await message.answer(
            f"Sizning referal linkingiz:\n "
            f"https://t.me/{SETTINGS.BOT_URL}/?start={user.referral}",
            reply_markup=users.home_reply_keyboard()
        )
    else:
        new_referral = str(uuid.uuid4())
        await user.update(referral=new_referral)

        await state.clear()
        await message.answer(
            f"Sizning referal linkingiz:\n "
            f"https://t.me/converter_uzbbot/?start={new_referral}",
            reply_markup=users.home_reply_keyboard()
        )



