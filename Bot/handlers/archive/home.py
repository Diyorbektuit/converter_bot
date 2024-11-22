from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Bot.keyboards.users import archive_keyboard

router = Router()

@router.message(lambda message: message.text == "📦 Fayllarni arxivlash yoki arxivdan chiqarish")
async def convert_archive(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        f"Arxivlash va arxivdan chiqarishni quyidagi turlardan\n "
        f"birini tanlashingiz mumkin",
        parse_mode='HTML' ,
        reply_markup=archive_keyboard()
    )
