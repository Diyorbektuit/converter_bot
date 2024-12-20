from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Bot.states.user import ArchiveState
from Bot.keyboards.users import home_reply_keyboard, archive_keyboard


router = Router()

# rar
@router.message(lambda message: message.text == "📂 RAR arxivdan chiqarish")
async def convert_zip_handler(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        text="Tez orada bu funksiya ishga tushadi",
        reply_markup=archive_keyboard()
    )

@router.message(ArchiveState.rar_to_file)
async def handle_file(message: Message, state: FSMContext):
    if message.text == "⬅️ Orqaga qaytish":
        await state.clear()
        return await message.answer("🔄Fayllarni arxivlash va arxivdan chiqarish",
                                    reply_markup=archive_keyboard())
    elif message.text == "🏠 Asosiy sahifaga qaytish":
        await state.clear()
        return await message.answer("Asosiy sahifa",
                                    reply_markup=home_reply_keyboard())

    await message.answer(f"Bu funksiya tez orada ishga tushadi", reply_markup=archive_keyboard())

