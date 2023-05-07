from PIL import Image
from fpdf import FPDF
import os

# Folder containing the input images
img_dir = r"C:\Users\priya\Documents\imgTopdf\images"


pdf = FPDF("P", "mm", "A4") #P/L orientation portrait/landscape


for img_file in os.listdir(img_dir):
    if img_file.endswith(".jpg") or img_file.endswith(".jpeg") or img_file.endswith(".png") or img_file.endswith(".bmp"):

        img_path = os.path.join(img_dir, img_file)
        img = Image.open(img_path)

        img.thumbnail((pdf.w, pdf.h)) #resizing, maintain a.r.

        pdf.add_page()     #centrize img
        x = (pdf.w - img.width) / 2
        y = (pdf.h - img.height) / 2
        pdf.image(img_path, x=x, y=y, w=img.width, h=img.height)

#saving..
pdf_path = os.path.join(img_dir, "..", "pdfs", "combined.pdf")
pdf.output(pdf_path, "F")
