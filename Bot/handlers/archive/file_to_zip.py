from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.utils import bot
from Bot.keyboards.users import archive_finish
from Bot.states.archive import ArchiveState
from Bot.keyboards.users import home_reply_keyboard, archive_keyboard
from utils.archive import convert_zip
from datetime import datetime

user_files = {}
router = Router()

# zip
@router.message(lambda message: message.text == "zip ko'rinishida arxivlash")
async def convert_zip_handler(message: Message, state: FSMContext):
    await state.set_state(ArchiveState.file_to_zip)

    await message.answer(
        text="arxivlamoqchi bolgan fayllaringizni yuboring",
        reply_markup=archive_finish()
    )

@router.message(ArchiveState.file_to_zip)
async def handle_file(message: Message, state: FSMContext):
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("🔄Fayllarni arxivlash va arxivdan chiqarish",
                                    reply_markup=archive_keyboard())
    elif message.text == "Asosiy sahifa":
        await state.clear()
        return await message.answer("Asosiy sahifa",
                                    reply_markup=home_reply_keyboard())
    elif message.text == "yakunlash":
        await state.clear()
        user_id = message.from_user.id

        if user_id not in user_files or not user_files[user_id]:
            await message.answer("Siz hech qanday fayl yubormadingiz.")
            return

        file_list = []
        today = datetime.today()
        for file_info in user_files[user_id]:
            file_id = file_info["file_id"]
            first_file_name = file_info['file_name']

            file = await bot.get_file(file_id)
            file_path = file.file_path
            file_name = first_file_name
            file_list.append(file_name)
            await bot.download_file(file_path, f"./downloads/{file_name}")
            await message.answer(f"Fayl yuklab olindi : {first_file_name}")

        convert_zip(file_list, f"archive-{str(today.month)}-{str(today.day)}-"
                         f"{str(today.minute)}-{str(today.second)}.zip")

        return await message.answer("Barcha fayllar qabul qilindi va saqlandi!")

    user_id = message.from_user.id
    file_id = message.document.file_id
    file_name = message.document.file_name

    if user_id not in user_files:
        user_files[user_id] = []

    user_files[user_id].append({"file_id": file_id, "file_name": file_name})
    await message.answer(f"Fayl qabul qilindi: {file_name}")

