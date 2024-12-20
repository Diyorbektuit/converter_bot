from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from Bot.keyboards import users, offer
from Bot.states.user import Offer

router = Router()


@router.callback_query(F.data == "converter")
async def converter_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()

    await callback.answer(
        "Qaysi turdan qaysi turga o'tmoqchi ekaningizni tanlang👇",
    )

    return await callback.message.answer(
        text="Fayllarni turini o'zgartirish",
        reply_markup=users.convert_reply_keyboard()
    )

@router.callback_query(F.data == "archive")
async def converter_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()

    await callback.message.answer(
        f"Arxivlash va arxivdan chiqarishni quyidagi turlardan\n "
        f"birini tanlashingiz mumkin",
        parse_mode='HTML',
        reply_markup=users.archive_keyboard()
    )

@router.callback_query(F.data == "other")
async def other_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Offer.message)

    return await callback.message.answer(
        text="Hali Boshqa xizmat turlari botimizga qoshilmadi \n"
             "lekin siz o'z taklifingizni qoldirishingiz mumkin \n"
             "biz albatta uni korib chiqib sizga kerakli xizmat \n"
             "turini botimizga qoshishga harakat qilamiz \n\n"
             "quyida Taklifningizni oddiy yozuv yoki \n"
             "ovozli xabar ko'rinishida yuborishingiz mumkin ",
        parse_mode='HTML',
        reply_markup=offer.offer_reply_keyboard()
    )

