import os
import subprocess

def pdf_covert(docx_path: str) -> dict:
    output_pdf = os.path.splitext(docx_path)[0] + ".pdf"
    try:
        message = subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            docx_path,
            "--outdir",
            os.path.dirname(docx_path)],
            check=True)

        return {
            'message': message,
            'output_pdf': output_pdf
        }
    except:
        return {
            'message': "error",
        }

