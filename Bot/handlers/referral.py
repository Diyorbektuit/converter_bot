from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import bot, checkmember
from Database.Tables import User, UserReferral
from ..keyboards import users, channels

router = Router()

@router.message(lambda message: message.text == "🗣Referall link olish")
async def offer_first(message: Message, state: FSMContext):
    if not await checkmember(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
    await state.clear()
    await state.set_state(Offer.message)
    await message.answer(
        "Sizning referal linkingiz: @converter_uzbbot/",
        reply_markup=offer.offer_reply_keyboard()
    )

