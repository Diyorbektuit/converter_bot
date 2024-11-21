from .home import router as home_router
from .pptx import router as pptx_router
from .docx import router as docx_router
from .pdf import router as pdf_router
from utils.utils import dp

dp.include_router(home_router)
dp.include_router(pptx_router)
dp.include_router(docx_router)
dp.include_router(pdf_router)