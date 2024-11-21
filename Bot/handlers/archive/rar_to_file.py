from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import bot
from Bot.keyboards.users import archive_finish
from Bot.states.archive import ArchiveState
from Bot.keyboards.users import home_reply_keyboard, archive_keyboard


router = Router()

# rar
@router.message(lambda message: message.text == "rar arxivdan chiqarish")
async def convert_zip_handler(message: Message, state: FSMContext):
    await state.set_state(ArchiveState.file_to_zip)

    await message.answer(
        text="arxivlamoqchi bolgan fayllaringizni yuboring",
        reply_markup=archive_finish()
    )

@router.message(ArchiveState.rar_to_file)
async def handle_file(message: Message, state: FSMContext):
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("🔄Fayllarni arxivlash va arxivdan chiqarish", reply_markup=archive_keyboard())
    elif message.text == "Asosiy sahifa":
        await state.clear()
        return await message.answer("Asosiy sahifa",
                                    reply_markup=home_reply_keyboard())


    await message.answer(f"Fayl qabul qilindi")

