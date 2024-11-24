from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from Bot.keyboards.inline import service_buttons
from Bot.keyboards.offer import offer_reply_keyboard
from Bot.keyboards.users import archive_keyboard
from Bot.keyboards import users, channels
from Bot.states.user import Offer

router = Router()

@router.message(lambda message: message.text == "📂 Fayl turini o'zgartirish")
async def convert(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Qaysi turdan qaysi turga o'tmoqchi ekaningizni tanlang",
        reply_markup=users.convert_reply_keyboard()
    )


@router.message(lambda message: message.text == "📦 Fayllarni arxivlash yoki arxivdan chiqarish")
async def convert_archive(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        f"Arxivlash va arxivdan chiqarishni quyidagi turlardan\n "
        f"birini tanlashingiz mumkin",
        parse_mode='HTML' ,
        reply_markup=archive_keyboard()
    )

@router.message(lambda message: message.text == "🔧 Xizmatlar ro'yxati")
async def services_handler(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(f"✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz!\n"
                                f"👇 Quydagi Ijtimoiy tarmoqlardan birini tanlang.",
        reply_markup=service_buttons(),
        parse_mode='HTML'
    )


@router.message(lambda message: message.text == '✉️ Taklif va fikr bildirish')
async def offer_first(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Offer.message)
    await message.answer(
        "Taklifningizni oddiy yozuv yoki ovozli xabar ko'rinishida yuborishingiz mumkin",
        reply_markup=offer_reply_keyboard()
    )