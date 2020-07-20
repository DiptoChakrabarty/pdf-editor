from PyPDF2 import PdfFileReader
from pathlib import Path
import os


path=  os.environ["PWD"] + "/terms.pdf"

with open(path,'rb') as f:
    pdf = PdfFileReader(f)
    info = pdf.getDocumentInfo()
print("Author: \t", info.author)
print()
print("Creator: \t", info.creator)
print()
print("Producer: \t",info.producer)
print()
print("Subject: \t", info.subject)
print()
print("title: \t",info.title)
print()
print("Number of Pages in pdf: \t",number_of_pages)


