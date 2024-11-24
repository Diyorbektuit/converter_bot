from .file_to_zip import router as zip_router
from .file_to_rar import router as rar_router
from .zip_to_file import router as zip_to_file_router
from .rar_to_file import router as rar_to_file_router
from utils.utils import dp

dp.include_router(zip_router)
dp.include_router(rar_router)
dp.include_router(zip_to_file_router)
dp.include_router(rar_to_file_router)
