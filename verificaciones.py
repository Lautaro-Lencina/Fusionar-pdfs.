from datetime import datetime
#coreo electronico
h = input("coloque su coreo electonico: ")
while "@gmail.com" not in h:
        print("su coreo no es valido")
        h = input("su correo no es valido:")

#verificar DNI
n = input("coloca su DNI: ")
n = n.replace(".","")
while len(n) != 8:
    print("su DNI es invalido")
    n = input("coloca su DNI: ")

print("su dni es valido")
#verificar si es mayor de edad
hoy = datetime.now()
dia = datetime.strftime(hoy,"%d")
mes = datetime.strftime(hoy,"%m")
año = datetime.strftime(hoy,"%Y")
año = int(año)
mes = int(mes)
dia = int(dia)
print("coloque su fecha de nacimiento")
dia2 = int(input("dia: "))
mes2 = int(input("mes: "))
año2 = int(input("año: "))

if año2 < año -18:
    print("erers mayor")
elif año2 == año -18:
    if mes2 < mes:
        print("erers mayor")
    elif mes2 == mes:
        if dia2 <= dia:
            print("tienes la mayoria de edad")
        else:
            print("eres menor de edad")
    else:
            print("eres menor de edad")
else:
     print("eres menor de edad")