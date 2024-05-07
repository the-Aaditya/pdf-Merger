import PyPDF2
from PyPDF2 import PdfWriter

num_of_pages = int(input("How many pdf you want to mearge: "))
merger = PdfWriter()
d=[]
for i in range(num_of_pages):
    d1 = input(f"Enter the path of the pdf no. {i+1}: ")
    d.append(d1)
for value in d:
    merger.append(value.strip())

pdname=input("name the pdf: ")
merger.write(pdname+".pdf")
merger.close()
