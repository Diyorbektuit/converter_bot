from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from utils.utils import bot, checkmember
from ..keyboards import users, channels
from Database.Tables import User, UserReferral

router = Router()


@router.callback_query(F.data == "check")
async def check_member(call: CallbackQuery):
    if await checkmember(call.from_user.id):

        await bot.send_message(chat_id=call.message.chat.id,
                               text="Marhamat quyidagi tugmalardan birini bosing",
                               reply_markup=users.home_reply_keyboard())
    else:
        await call.answer(text="Siz kanalga a'zo bolmadingiz")


@router.message(Command(commands=['start']))
async def start(message: Message):
    text_parts = message.text.split()

    referral = str(text_parts[1]) if len(text_parts) > 1 else None

    kwargs = {
        'username': message.from_user.username,
        'full_name': message.from_user.full_name
    }

    user = await User.get_or_create(telegram_id=message.from_user.id, **kwargs)

    if user is None:
        return await message.answer(text="Siz bu botdan foydalana olmaysiz")

    if not await checkmember(message.from_user.id):
        return await message.answer(
            text="Botdan foydalanish uchun quyidagi kanalga a'zo boling",
            reply_markup=channels.channels_buttons()
        )

    if referral is not None:
        referred_user = await User.get(referral=referral)
        print(f"Referred User: {referred_user}")
        if referred_user:
            user_referral = await UserReferral.create(
                user_id=referred_user.id,
                offered_user_id=user.id
            )
            referred_user_wallet = referred_user.wallet
            new_wallet = referred_user_wallet + user_referral.point
            await referred_user.update(wallet=new_wallet)

    await message.answer(
        f"Xush kelibsiz, {message.from_user.full_name}!",
        reply_markup=users.home_reply_keyboard()
    )



