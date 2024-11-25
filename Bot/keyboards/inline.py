from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def service_buttons() -> InlineKeyboardMarkup:
    button_change_file_type = InlineKeyboardButton(
        text="🔄 Fayl turini o'zgartirish", callback_data="converter"
    )
    button_archive_files = InlineKeyboardButton(
        text="📦 Fayllarni arxivlash / chiqarish", callback_data="archive"
    )
    button_other_services = InlineKeyboardButton(
        text="⚙️ Boshqa xizmatlar", callback_data="other"
    )

    reply = InlineKeyboardMarkup(inline_keyboard=[
        [button_change_file_type],  # Fayl turini o'zgartirish tugmasi
        [button_archive_files],  # Fayl arxivlash va chiqarish tugmasi
        [button_other_services],  # Boshqa xizmatlar tugmasi
    ])

    return reply

