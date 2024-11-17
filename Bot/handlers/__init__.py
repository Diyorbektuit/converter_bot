from .start import router as start_router
from .offer import router as offer_router
from .convert import router as convert_router
from .back import router as back_router
from .referral import router as referral_router
from .balance import router as balance_router
from .services import router as services_router
from utils.utils import dp

dp.include_router(start_router)
dp.include_router(offer_router)
dp.include_router(convert_router)
dp.include_router(back_router)
dp.include_router(referral_router)
dp.include_router(balance_router)
dp.include_router(services_router)