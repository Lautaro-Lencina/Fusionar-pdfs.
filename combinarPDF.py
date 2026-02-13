import os
from tkinter import Tk, filedialog, messagebox
from PyPDF4 import PdfFileMerger

Tk().withdraw()#oculta ventana principal
messagebox.showinfo("","coloque la carpeta con los pdfs.(nota: el orden es segun como esten en la carpeta)")
carpeta_entrada = filedialog.askdirectory()
#lee la carpeta donde esta el programa 
    
def fucionpdf(carpeta_entrada, archivo_salida = 'fucion.pdf'):
    if carpeta_entrada:
     pdfs = []
     mango = PdfFileMerger()
    
     for archivo in os.listdir(carpeta_entrada):
      if archivo[-4:] == ".pdf":
        pdfs.append(archivo)
        ruta = carpeta_entrada + '\\' + archivo
        with open(ruta, 'rb') as fileobj:
                mango.append(fileobj)
     archivo_salida = os.path.join(carpeta_entrada, archivo_salida)#solucion de error de la ruta
     mango.write(archivo_salida)
     mango.close()
fucionpdf(carpeta_entrada)
