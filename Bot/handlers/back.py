from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.utils import check_member
from ..keyboards.channels import channels_buttons
from ..keyboards.users import home_reply_keyboard
from aiogram import Router

router = Router()

@router.message(lambda message: message.text == '⬅️Orqaga', )
async def back(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels_buttons())
    await state.clear()
    await message.answer(
        "Asosiy sahifa",
        reply_markup=home_reply_keyboard()
    )
