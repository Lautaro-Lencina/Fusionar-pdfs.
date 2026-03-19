import os
from tkinter import *
from tkinter import Tk, filedialog
from PyPDF4 import PdfFileMerger

ak = False
def activar():
 global ak
 ak = True

ventana = Tk()
ventana.title("fucuinar PDFs")
ventana.minsize(width=300, height=400)
ventana.config(padx=35, pady= 35)

ventana.iconbitmap("1.ico")
ventana.configure(bg="light blue")

canvas= Canvas(width=330, height=330)
foto= PhotoImage(file="mi.png")
canvas.create_image(170, 170, image=foto)
canvas.grid(column=0, row= 0)

etiqueta1 =Label(text= "coloque la carpeta con los pdfs.", font=("Arial",14))

etiqueta1.configure(fg="grey12", bg="light blue")
etiqueta1.grid(column=0, row=2)

etiqueta2 =Label(text= "(nota: el orden es segun como esten en la carpeta).", font=("Arial",14))
etiqueta2.grid(column=0, row=3)
etiqueta2.configure(fg="gray12", bg="light blue")
boton1 = Button(text="buscar", font=("Arial",14), command= activar)
boton1.configure(fg="gray12", bg="steel blue")
boton1.grid(column=0, row= 4)

while not ak:
  ventana.update() 
if ak == True:
   carpeta_entrada = filedialog.askdirectory()
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
ventana.mainloop()
