from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Database.Tables import User, UserReferral

router = Router()

@router.message(lambda message: message.text == "💰Mening hisobim")
async def balance(message: Message, state: FSMContext):
    await state.clear()
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
    referrals = await UserReferral.filter(user_id=user.id)

    await message.answer(
        f"Sizning hisobingizda <b>{user.wallet}</b> so'm bor\n "
        f"<b> {len(referrals)} </b> ta odam taklif qilgansiz",
        parse_mode='HTML'  # 'html' ni 'HTML' ga o'zgartirdik
    )
