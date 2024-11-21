from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from utils.utils import bot
from Bot.keyboards.users import archive_finish
from Bot.states.archive import ArchiveState
from Bot.keyboards.users import home_reply_keyboard, archive_keyboard
from utils.archive import create_rar_archive
import os
from datetime import datetime

user_files = {}
base_dir = "/home/diyorbek/PycharmProjects/converter_bot/downloads"
router = Router()


# zip
@router.message(lambda message: message.text == "rar ko'rinishda arxivlash")
async def convert_zip_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.set_state(ArchiveState.file_to_rar)

    if user_id in user_files.keys():
        user_files.update({
            user_id: []
        })

    await message.answer(
        text="arxivlamoqchi bolgan fayllaringizni yuboring",
        reply_markup=archive_finish()
    )


@router.message(ArchiveState.file_to_rar)
async def handle_file(message: Message, state: FSMContext):
    user_id = message.from_user.id
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

        if user_id not in user_files.keys():
            await message.answer("Siz hech qanday fayl yubormadingiz.")
            return

        file_list = []

        for file_info in user_files[user_id]:
            file_path = file_info['file_path']

            file_list.append(file_path)

        today = datetime.today()
        archive_name = f"downloads/archive/rar-{user_id}-{str(today.month)}-{str(today.day)}-{str(today.minute)}-{str(today.second)}.rar"

        await message.answer("Tayyorlanmoqda ...")

        rar_path = create_rar_archive(file_list, archive_name)
        if rar_path is None:
            for file_path in file_list:
                os.remove(file_path)
            user_files.update({
                user_id: []
            })
            await state.clear()
            return await message.answer("Xatolik yuz berdi boshqattan urinib ko'ring /start")
        send_file = FSInputFile(path=rar_path)
        await message.answer_document(send_file)
        os.remove(rar_path)
        for file_path in file_list:
            os.remove(file_path)
        user_files.update(
            {
                user_id: []
            }
        )
        return await message.answer("Bizning xizmatdan foydalanganingiz uchun rahmat 😊",
                                    reply_markup=archive_keyboard())

    if message.document:
        document = message.document
        file_name = document.file_name
        file_path = f"{base_dir}/{file_name}"

        file = await bot.get_file(document.file_id)
        await bot.download_file(file.file_path, file_path)
        if not user_id in user_files.keys():
            user_files[message.from_user.id] = []
        user_files[message.from_user.id].append({"file_path": file_path})
        await message.answer(f"Hujjat qabul qilindi")

    elif message.photo:
        photo = message.photo[-1]
        file_name = f"photo_{photo.file_id}.jpg"
        file_path = f"{base_dir}/{file_name}"

        file = await bot.get_file(photo.file_id)
        await bot.download_file(file.file_path, file_path)
        if not user_id in user_files.keys():
            user_files.update({
                user_id: []
            })
        user_files[user_id].append({"file_path": file_path})
        await message.answer(f"Rasm qabul qilindi")

    elif message.video:
        video = message.video
        file_name = video.file_name or f"video_{video.file_id}.mp4"
        file_path = f"{base_dir}/{file_name}"

        file = await bot.get_file(video.file_id)
        await bot.download_file(file.file_path, file_path)
        if not user_id in user_files.keys():
            user_files[user_id] = []
        user_files[message.from_user.id].append({"file_path": file_path})
        await message.answer(f"Video qabul qilindi")


