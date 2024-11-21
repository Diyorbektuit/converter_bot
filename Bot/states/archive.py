from aiogram.fsm.state import State, StatesGroup

class ArchiveState(StatesGroup):
    file_to_zip = State()
    zip_to_file = State()
    file_to_rar = State()
    rar_to_file = State()
