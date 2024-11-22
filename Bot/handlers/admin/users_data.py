from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils.utils import check_member
from Bot.keyboards import users, channels
from Database.Tables import User
from datetime import datetime, timedelta

router = Router()

@router.message(lambda message: message.text == "👥 Foydalanuvchilar haqida ma'lumot")
async def users_data_handler(message: Message, state: FSMContext):
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

