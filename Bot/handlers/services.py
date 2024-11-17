from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Database.Tables import User, UserReferral
from ..keyboards import inline

router = Router()

@router.message(lambda message: message.text == "🗂Xizmatlar")
async def services(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz!\n"
                                f"👇 Quydagi Ijtimoiy tarmoqlardan birini tanlang.",
        reply_markup=inline.service_buttons(),
        parse_mode='HTML'
    )

@router.callback_query(F.data == "converter")
async def converter(callback: CallbackQuery, state: FSMContext):
    await state.clear()

    return callback.answer(
        "Qaysi turdan qaysi turga o'tmoqchi ekaningizni tanlang👇",
    )


