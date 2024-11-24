from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.settings import SETTINGS
from Database.Tables import User
from Bot.keyboards import users, channels
import uuid

router = Router()

@router.message(lambda message: message.text == "🔗 Referal havolani olish")
async def offer_first(message: Message, state: FSMContext):
    kwargs = {
        'username': message.from_user.username,
        'full_name': message.from_user.full_name
    }

    user = await User.get_or_create(telegram_id=message.from_user.id, kwargs=kwargs)
    if user is None:
        return await message.answer(
            "Siz botda hali ro'yhatdan o'tmagansiz \n"
            " iltimos \start tugmasini bosing"
        )
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



