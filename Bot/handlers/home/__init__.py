from .admin import router as admin_router
from .user import router as user_router
from utils.utils import dp

dp.include_routers(admin_router, user_router)