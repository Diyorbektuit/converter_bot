from aiogram.fsm.state import State, StatesGroup

class Offer(StatesGroup):
    message = State()