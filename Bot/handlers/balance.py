from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Database.Tables import User, UserReferral

router = Router()

@router.message(lambda message: message.text == "💰Mening hisobim")
async def balance(message: Message, state: FSMContext):
    await state.clear()
    user = await User.get(telegram_id=message.from_user.id)
    referrals = await UserReferral.filter(user_id=user.id)

    # HTML formatida yuboriladigan matnni o'zgartirdik
    await message.answer(
        f"Sizning hisobingizda <b>{user.wallet}</b> so'm bor\n "
        f"<b> {len(referrals)} </b> ta odam taklif qilgansiz",
        parse_mode='HTML'  # 'html' ni 'HTML' ga o'zgartirdik
    )
