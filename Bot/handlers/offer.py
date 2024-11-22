from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ..states.offer import Offer
from utils.utils import bot, check_member, ADMIN
from Database.Tables import UserOffer, User
from ..keyboards import users, channels, offer

router = Router()

@router.message(lambda message: message.text == '✉️ Taklif va fikr bildirish')
async def offer_first(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    await state.clear()
    await state.set_state(Offer.message)
    await message.answer(
        "Taklifningizni oddiy yozuv yoki ovozli xabar ko'rinishida yuborishingiz mumkin",
        reply_markup=offer.offer_reply_keyboard()
    )

@router.message(Offer.message, lambda message: message.voice or None)
async def audio_offer(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    user = await User.get(
        telegram_id=message.from_user.id
    )

    if user is not None:
        new_user = await UserOffer.create(
            user=user,
            file=message.voice.file_id
        )

    response = (f"Yangi taklif keldi \n"
                f"Taklif egasi idsi: {message.chat.id} \n"
                f"Xabar kelgan sana: {message.date} \n"
                f"Foydalanuvchi ismi: {message.from_user.full_name} \n"
                f"Foydalanuvchi username: @{message.from_user.username}\n")

    await message.reply("Taklifingiz yuborildi,taklifingiz uchun rahmat😊", reply_markup=users.home_reply_keyboard())
    await state.clear()
    await bot.send_voice(chat_id=int(ADMIN), voice=message.voice.file_id, caption=response)



@router.message(Offer.message, lambda message: message.text or None)
async def text_offer(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    if message.text == "⬅️Orqaga":
        await state.clear()
        return await message.answer("Asosiy sahifa", reply_markup=users.home_reply_keyboard())

    user = await User.get(
        telegram_id=message.from_user.id
    )

    if user is not None:
        await UserOffer.create(
            user=user,
            file=message.text
        )

    response = (f"Yangi taklif keldi \n "
                f"taklif egasi idsi : {message.chat.id} \n "
                f"Xabar kelgan sana {message.date} \n "
                f"foydalnuvchi ismi: {message.from_user.full_name} \n "
                f"foydalanuvchi username: @{message.from_user.username}\n"
                f"Takif: {message.text}")

    await message.reply("Taklifingiz yuborildi,taklifingiz uchun rahmat😊", reply_markup=users.home_reply_keyboard())
    await state.clear()
    await bot.send_message(chat_id=int(ADMIN), text=response)
