from aiogram.fsm.state import State, StatesGroup

class ConvertState(StatesGroup):
    pdf = State()
    pptx = State()
    docx = State()