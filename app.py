import PyPDF2
from pathlib import Path
import os


path=  os.environ["PWD"] + "/terms.pdf"
print(path)
pdffile = open(path,'rb')

pdf = PyPDF2.PdfFileReader(pdffile)
print(pdf.numPages)

first = pdf.getPage(0)
print(first.extractText())



'''with open(path,'rb') as f:
    pdf = PdfFileReader(f)
    info = pdf.getDocumentInfo()
    first = pdf.getPage(0)
print(first.extractText())
print("Author: \t", info.author)
print()
print("Creator: \t", info.creator)
print()
print("Producer: \t",info.producer)
print()
print("Subject: \t", info.subject)
print()
print("title: \t",info.title)
print()'''



