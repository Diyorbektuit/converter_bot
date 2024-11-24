from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Bot.keyboards.users import home_reply_keyboard
from aiogram import Router

router = Router()

@router.message(lambda message: message.text == '🏠 Asosiy sahifaga qaytish')
async def back(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Asosiy sahifa",
        reply_markup=home_reply_keyboard()
    )
