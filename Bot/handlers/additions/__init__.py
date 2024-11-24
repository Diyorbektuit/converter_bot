from utils.utils import dp
from .back import router as back_router
from .offer import router as offer_router
from .start import router as start_router
from .services import router as services_router
from .referral import router as referral_router
from .balance import router as balance_router

dp.include_routers(back_router, offer_router, start_router, services_router, referral_router, balance_router)