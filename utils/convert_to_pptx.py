import os
from pdf2image import convert_from_path
from pptx import Presentation
from pptx.util import Inches


def convert_file_to_pptx(pdf_path):
    pptx_path = os.path.splitext(pdf_path)[0] + ".pptx"
    # PDF sahifalarini tasvirlarga aylantirish
    images = convert_from_path(pdf_path)

    # Yangi PowerPoint prezentatsiyasi yaratish
    presentation = Presentation()

    for image in images:
        # Har bir sahifani yangi slaydga qo'shish
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])

        # Sahifani slaydga joylash
        image.save("temp.jpg", "JPEG")
        slide.shapes.add_picture("temp.jpg", Inches(0), Inches(0),
                                 width=presentation.slide_width,
                                 height=presentation.slide_height)

    # Prezentatsiyani saqlash
    presentation.save(pptx_path)

    return pptx_path

