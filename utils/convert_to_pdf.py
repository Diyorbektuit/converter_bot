import os
import subprocess

def pdf_covert(docx_path):
    output_pdf = os.path.splitext(docx_path)[0] + ".pdf"

    subprocess.run([
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        docx_path,
        "--outdir",
        os.path.dirname(docx_path)],
        check=True)

    return output_pdf