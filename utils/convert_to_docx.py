import os
from pdf2docx import Converter

def convert_file_to_docx(pdf_path: str) -> str:
    docx_path = os.path.splitext(pdf_path)[0] + ".docx"
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return docx_path
