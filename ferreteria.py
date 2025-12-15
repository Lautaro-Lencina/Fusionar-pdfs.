
articulos = []
apagado = False
while True:
   
   if apagado == True:
     break
   else:
    n = input("desea buscar o colocar una herramienta: ").lower()
    if n != "buscar" and n != "colocar":
     print("error por favor, diga si quiere colocar o buscar")
    elif n == "colocar":
      while True:
         herramienta = input("colocar herramienta: ").lower()
         cantidad = input("coloque cuantos son: ")
         x = [herramienta,"cantidad:",cantidad]
         x = " ".join(x)
         articulos.append(x)
         continuar = input("deseas colocar otro articulo? si/no: ")
         if continuar != "si":
           ahora = input("deseas finalizar?si/no: ").lower()
           if ahora != "no":
             apagado = True
             break
           else:
             break

    else:
      while True:
        herramientas = input("coloque que articulo quiere buscar: ").lower()
        encontrado = False
        for palabra in articulos:
         if herramientas in palabra: 
          print("su articulo fue encontrado:")
          print(palabra)
          encontrado = True
          break
        if encontrado:
         con = input("desea buscar otro articulo?si/no:  ").lower()
         if con != "si":
              ahora = input("deseas finalizar?si/no: ").lower()
              if ahora != "no":
               apagado = True
               break
              else:
               break 
         else:
           encontrado = False

        else:
          print("no se encuentra ese articulo") 
          j = input("desea buscar otro articulo?, si o no?: ").lower()

          if j != "si":
              ahora = input("deseas finalizar?si/no: ").lower()
              if ahora != "no":
               apagado = True
               break
              else:
               break
          else:
           herramientas = input("coloque que articulo quiere buscar: ").lower()