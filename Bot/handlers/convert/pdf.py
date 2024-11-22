from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import os

from utils.utils import check_member, bot
from utils.convert_to_pdf import pdf_covert
from Bot.keyboards import users, channels
from Bot.states.convert import ConvertState

router = Router()

@router.message(lambda message: message.text == "📄 Faylni PDF formatiga o'zgartirish")
async def convert_pdf_handler(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    elif message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    await state.set_state(ConvertState.pdf)
    await message.answer(
        "ppt, pptx, doc, docx turidagi fayl yuboring va u pdf aylantiriladi",
        reply_markup=users.convert_reply_keyboard()
    )

@router.message(ConvertState.pdf, lambda message: message)
async def convert_to_pdf(message: Message, state: FSMContext):
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    document = message.document
    file_info = await bot.get_file(document.file_id)
    file_path = f"downloads/{document.file_name}"

    await message.answer("Tekshirilmoqda...")

    await bot.download_file(file_info.file_path, file_path)

    if file_path.endswith(('.ppt', '.pptx', '.doc', '.docx')):
        response = pdf_covert(file_path)
        if response.get("message") == "error":
            os.remove(file_path)
            return message.answer(
                text="xatolik yuz berdi fayl qulflangan bo'lishi mumkin \n"
                     "muammo uchun uzr so'raymiz"
            )
        new_file_path = response.get('output_pdf')
        await message.answer("Tayyorlanmoqda ozgina kuting...")
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

