from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from utils.utils import bot
from Bot.keyboards import users
from Database.Tables import User, UserReferral

router = Router()


@router.callback_query(F.data == "check")
async def check_member_handler(call: CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id,
                           text="Bizning xizmatimizni tanlaganingiz uchun rahmat😊",
                           reply_markup=users.home_reply_keyboard())


@router.message(Command(commands=['start']))
async def start_handler(message: Message):
    text_parts = message.text.split()

    referral = str(text_parts[1]) if len(text_parts) > 1 else None

    kwargs = {
        'username': message.from_user.username,
        'full_name': message.from_user.full_name
    }

    user = await User.get_or_create(telegram_id=message.from_user.id, **kwargs)

    if user is None:
        return await message.answer(
            text="Uzr, siz ushbu botdan foydalanishga ruxsat olmadingiz. Qo‘llab-quvvatlash xizmatiga murojaat qiling.")

    if user.role == "admin":
        return await message.answer(
            f"Assalomu alaykum, hurmatli admin {message.from_user.full_name}! Ishlaringizga omad! 👋",
            reply_markup=users.home_reply_keyboard_admin()
        )

    if referral is not None:
        referred_user = await User.get(referral=referral)
        if referred_user:
            user_referral = await UserReferral.create(
                user_id=referred_user.id,
                offered_user_id=user.id
            )
            referred_user_wallet = referred_user.wallet
            new_wallet = referred_user_wallet + user_referral.point
            await referred_user.update(wallet=new_wallet)

    await message.answer(
         f"Xush kelibsiz, {message.from_user.full_name}! 😊 Bizning xizmatimizdan foydalanishingizdan xursandmiz.",
        reply_markup=users.home_reply_keyboard()
    )



