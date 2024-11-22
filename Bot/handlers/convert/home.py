from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import check_member
from Bot.keyboards import users, channels

router = Router()

@router.message(lambda message: message.text == "📂 Fayl turini o'zgartirish")
async def convert(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())

    await state.clear()
    await message.answer(
        "Qaysi turdan qaysi turga o'tmoqchi ekaningizni tanlang",
        reply_markup=users.convert_reply_keyboard()
    )

