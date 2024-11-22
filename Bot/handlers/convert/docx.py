from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import os
from utils.utils import check_member, bot
from utils.convert_to_docx import convert_file_to_docx
from Bot.keyboards import users, channels
from Bot.states.convert import ConvertState

router = Router()

@router.message(lambda message: message.text == "📃 Faylni DOCX formatiga o'zgartirish")
async def convert_docx_handler(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    if message.text == "⬅️ Orqaga qaytish":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    await state.set_state(ConvertState.docx)
    await message.answer(
        "pdf turidagi fayl yuboring va u docx aylantiriladi",
        reply_markup=users.convert_reply_keyboard()
    )

@router.message(ConvertState.docx, lambda message: message)
async def convert_to_docx(message: Message, state: FSMContext):
    if message.text == "⬅️ Orqaga qaytish":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = f"downloads/{document.file_name}"

    await message.answer("Tekshirilmoqda...")

    await bot.download_file(file_info.file_path, file_path)

    if file_path.endswith(('.pdf',)):
        await message.answer("Tayyorlanmoqda ozgina kuting...")
        new_file_path = convert_file_to_docx(file_path)
    else:
        os.remove(file_path)
        return await message.answer(
            "Bunday turdagi hujjat qabul qilinmaydi \n"
            "Tekshirib boshqatdan yuboring"
        )


    new_file = types.FSInputFile(new_file_path)
    await message.answer_document(new_file)
    await state.clear()

    os.remove(file_path)
    os.remove(new_file_path)
