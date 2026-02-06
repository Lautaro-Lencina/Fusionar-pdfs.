import os
from PyPDF4 import PdfFileMerger
#lee la carpeta donde esta el programa
carpeta_entrada =  os.getcwd()

def fucionpdf(carpeta_entrada, archivo_salida = 'fucion.pdf'):

    pdfs = []
    mango = PdfFileMerger()
    for archivo in os.listdir(carpeta_entrada):
        if archivo[-4:] == ".pdf":
            pdfs.append(archivo)
    for pdf in pdfs:
        mango.append(str(pdf))
    mango.write(archivo_salida)
    mango.close()
fucionpdf(carpeta_entrada)
