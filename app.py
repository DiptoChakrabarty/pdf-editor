from PyPDF2 import PdfFileReader
from pathlib import Path
import os


pdf_path=  os.environ["PWD"] + "/samplepdf.pdf"

pdf = PdfFileReader(str(pdf_path))
pages= pdf.getNumPages()
print(pages)