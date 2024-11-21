from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import check_member, bot
from Bot.keyboards import users, channels
from Database.Tables import User
from .functions import send_message_to_all_users
from Bot.states.sen_message_users import MessageState

router = Router()

@router.message(lambda message: message.text == "hamma userlarga xabar jo'natish")
async def message_to_users(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    user = await User.get(telegram_id=message.from_user.id)
    if user.role != "admin":
        return message.answer(
        "Bunday buyruq mavjud emas",
        reply_markup=users.home_reply_keyboard()
    )
    await state.set_state(MessageState.first)
    await message.answer(
        "jonatmoqchi bolgan xabaringizni yuboring",
        reply_markup=users.home_reply_keyboard_admin(),
        parse_mode='HTML'
    )

@router.message(MessageState.first)
async def message_to_users(message: Message, state: FSMContext):
    if not await check_member(message.from_user.id):
        return await message.answer(text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
                                    reply_markup=channels.channels_buttons())
    user = await User.get(telegram_id=message.from_user.id)
    if user.role != "admin":
        return message.answer(
        "Bunday buyruq mavjud emas",
        reply_markup=users.home_reply_keyboard()
    )
    await state.clear()
    await message.answer(
        "Jarayon boshlandi...",
    )
    message_data = await send_message_to_all_users(text=message.text, bot=bot)
    await message.answer(
        f"muvafaqiyatli : <b> {message_data.get('success_count')} </b> ta\n"
        f"xatolik yuz berdi: <b> {message_data.get('error_count')} </b>",
        reply_markup=users.home_reply_keyboard_admin(),
        parse_mode='HTML'
    )
