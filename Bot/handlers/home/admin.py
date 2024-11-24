from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import bot
from Bot.keyboards import users, channels
from Database.Tables import User
from utils.utils import send_message_to_all_users
from datetime import datetime, timedelta
from Bot.states.admin import MessageState

router = Router()

@router.message(lambda message: message.text == "📨 Hamma foydalanuvchilarga xabar yuborish")
async def message_to_users(message: Message, state: FSMContext):
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

@router.message(lambda message: message.text == "👥 Foydalanuvchilar haqida ma'lumot")
async def users_data_handler(message: Message, state: FSMContext):
    user = await User.get(telegram_id=message.from_user.id)
    if user.role != "admin":
        return message.answer(
        "Bunday buyruq mavjud emas",
        reply_markup=users.home_reply_keyboard()
    )
    await state.clear()
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    users_data = await User.all_users()
    last_day_users = await User.all_users(start_date=yesterday, end_date=today)

    await message.answer(
        f"Hamma userlar soni: <b> {len(list(users_data))} </b>\n"
        f"Oxirgi kunda qo'shilganlar soni: <b> {len(list(last_day_users))} </b>",
        reply_markup=users.home_reply_keyboard_admin(),
        parse_mode='HTML'
    )

@router.message(MessageState.first)
async def message_to_users(message: Message, state: FSMContext):
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
    message_data = await send_message_to_all_users(text=message.text, bot_=bot)
    await message.answer(
        f"muvafaqiyatli : <b> {message_data.get('success_count')} </b> ta\n"
        f"xatolik yuz berdi: <b> {message_data.get('error_count')} </b>",
        reply_markup=users.home_reply_keyboard_admin(),
        parse_mode='HTML'
    )
