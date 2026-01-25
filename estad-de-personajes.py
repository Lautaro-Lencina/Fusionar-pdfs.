import random
def punto(x,puntos,estad, y):
   
   if x > 7:
      print("intenta usar menos puntos")
      return puntos, False
   elif x > puntos:
      print("puntos insuficiontes solo quedan ",puntos,"puntos")
      return puntos, False
   else:
      puntos = puntos - x
      estad[y] = estad[y] + x
      return puntos, True
def dado6():
  d_0 = []
  d_1 = random.randint(1,6)
  d_0 = d_0 + [d_1]
  d_2 = random.randint(1,6)
  d_0 = d_0 + [d_2]
  d_3 = random.randint(1,6)
  d_0 = d_0 + [d_3]
  d_4 = random.randint(1,6)
  d_0 = d_0 + [d_4]
  d_0.sort(reverse= True)
  resultado = d_0[:3]
  suma = sum(resultado)
  return suma

usuario = input("coloque su nombre por favor: ")
estadisticas = ""
print("para las estadisticas que modo quieres uasr? ")
print("1. tirada clasica(con dados de D6) ")
print("2. tirada estandar(con D20) ")
print("3. puntos para gastar ")
while True:
  
  desion_1 = int(input("cual elige?: "))

  if desion_1 == 1:
   print("empecemos con las tiradas")
   
   STR = dado6()
   DEX = dado6()
   CON = dado6()
   INT = dado6()
   WIS = dado6()
   CHA = dado6()
   z = ["Fuerza",STR,"Destreza",DEX,"Constitucion", CON,"Inteligencia",INT,"Sabiduria",WIS,"Carisma",CHA]
   z = str(z)
   estadisticas = z
   break

  elif desion_1 == 2:
    STR = random.randint(1,20)
    DEX = random.randint(1,20)
    CON = random.randint(1,20)
    INT = random.randint(1,20)
    WIS = random.randint(1,20)
    CHA = random.randint(1,20)
    z = ["Fuerza",STR,"Destreza",DEX,"Constitucion", CON,"Inteligencia",INT,"Sabiduria",WIS,"Carisma",CHA]
    z = str(z)
    estadisticas = z
    break

  elif desion_1 == 3:
    print("en esta opcion tienes para poner 27 puntos a la estaditicas que quieras.")
    print("todas las estadisticas empienzan en 8. y el maximo que puedes subir son 15")
    estad = {"STR":8,
    "DEX":8,
    "CAN":8, 
    "INT":8,
    "WIS":8,
    "CHA":8,
    }
    y = ""
    puntos = 27
    ATR = False
    while not ATR and puntos > 0:
     camilo = False 
     while not camilo and puntos > 0:

      nex = int(input("cuantos puntos quieres poner a fuerza: "))
      y = "STR"
      puntos, camilo = punto(nex, puntos, estad, y)
     camilo = False

     while not camilo and puntos > 0:
      nex = int(input("cuantos puntos quieres poner a defensa: "))
      y = "DEX"
      puntos,camilo = punto(nex, puntos, estad, y)
     camilo = False
     while not camilo and puntos > 0:
       nex = int(input("cuantos puntos quieres poner a inteligencia: "))
       y = "INT"
       puntos, camilo = punto(nex, puntos, estad, y)
     if puntos == 0:
               break
     
     else:
        camilo = False
        while not camilo and puntos > 0:
         nex = int(input("cuantos puntos quieres poner a sabiduria: "))
         puntos,camilo = punto(nex, puntos, estad, y)
         y = "WIS"
        if puntos == 0:
               break
        else:
          camilo = False
          while not camilo and puntos > 0:
           nex = int(input("cuantos puntos quieres poner a carisma: "))
           y = "CHA"
           puntos,camilo = punto(nex, puntos, estad, y)
          if camilo == True:
             ATR = True
    z = estad.items()
    z = str(z)
    estadisticas = z
    break

  else:
    print("su opcion no es validad")
print(estadisticas)
with open("estadisticas.txt", 'w') as archivo:
    archivo.write("el usuario ")
    archivo.write(usuario)
    archivo.write("\n")
    archivo.write("tiene estas estadisticas.\n")
    archivo.write(estadisticas)
    archivo.close()