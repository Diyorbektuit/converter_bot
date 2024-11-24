from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import os

from utils.utils import bot
from utils.convert_to_pptx import convert_file_to_pptx
from Bot.keyboards import users
from Bot.states.user import ConvertState

router = Router()

@router.message(lambda message: message.text == "📊 Faylni PPTX formatiga o'zgartirish")
async def convert_pptx_handler(message: Message, state: FSMContext):
    await state.set_state(ConvertState.pptx)
    await message.answer(
        "pdf turidagi fayl yuboring va u pptx aylantiriladi",
        reply_markup=users.convert_reply_keyboard()
    )

@router.message(ConvertState.pptx,lambda message: message)
async def convert_to_pptx(message: Message, state: FSMContext):
    if message.document:
        document = message.document
        file_info = await bot.get_file(document.file_id)
        file_path = f"downloads/{document.file_name}"

        await message.answer("Tekshirilmoqda...")

        await bot.download_file(file_info.file_path, file_path)

        if file_path.endswith(('.pdf', )):
            new_file_path = convert_file_to_pptx(file_path)
            await message.answer("Tayyorlanmoqda ozgina kuting...")
        else:
            os.remove(file_path)
            return await message.answer(
                "Bunday turdagi hujjat qabul qilinmaydi \n"
                "Tekshirib boshqatdan yuboring"
            )

        new_file = types.FSInputFile(new_file_path)
        await message.answer_document(new_file)

        os.remove(file_path)
        os.remove(new_file_path)
    return await message.answer(
        "Siz faqat pdf turdagi fayl yubora olasiz"
    )
