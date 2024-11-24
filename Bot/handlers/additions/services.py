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
        "Iltimos, qaysi turdan qaysi turga o‘zgartirmoqchi ekanligingizni tanlang👇",
    )

    return await callback.message.answer(
        text="🔄 Fayllar turini o‘zgartirish uchun kerakli opsiyani tanlang:",
        reply_markup=users.convert_reply_keyboard()
    )


@router.callback_query(F.data == "archive")
async def archive_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()

    return await callback.message.answer(
        text=(
            "📦 Arxivlash va arxivdan chiqarish xizmati uchun quyidagi formatlardan birini tanlang:"
        ),
        parse_mode='HTML',
        reply_markup=users.archive_keyboard()
    )


@router.callback_query(F.data == "other")
async def other_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Offer.message)

    return await callback.message.answer(
        text=(
            "📌 Hozircha boshqa xizmat turlari botimizga qo‘shilmagan.\n\n"
            "😊 Ammo, siz o‘z taklifingizni yuborishingiz mumkin! Biz uni ko‘rib chiqamiz "
            "va sizga kerakli xizmat turini botimizga qo‘shishga harakat qilamiz.\n\n"
            "📨 Taklifingizni oddiy yozuv yoki ovozli xabar shaklida yuborishingiz mumkin."
        ),
        parse_mode='HTML',
        reply_markup=offer.offer_reply_keyboard()
    )
