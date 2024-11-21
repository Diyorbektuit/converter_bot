from .users_data import router as users_router
from .message import router as message_router
from utils.utils import dp

dp.include_router(users_router)
dp.include_router(message_router)