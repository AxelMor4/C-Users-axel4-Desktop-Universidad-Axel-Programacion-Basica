enero = 0
febrero = 0
marzo = 0
abril = 0
mayo = 0 
junio = 0
julio = 0
agosto = 0
sep = 0
octu = 0
nov = 0
dic = 0
total_edades = 0
n_personas = int(input("Ingrese la cantidad de personas que va a registrar el mes de cumpleanos: "))

for i in range(n_personas):
    mes = input("Ingrese el mes de la persona: ")
    edad = int(input("Ingrese la edad que tiene:"))
    if mes == "enero":
        enero += 1
    elif mes == "febrero":
        febrero += 1
    elif mes == "marzo":
        marzo += 1
    elif mes == "abril":
        abril += 1
    elif mes == "mayo":
        mayo += 1
    elif mes == "junio":
        junio += 1
    elif mes == "julio":
        julio += 1
    elif mes == "agosto":
        agosto += 1
    elif mes == "septiembre":
        sep += 1
    elif mes == "octubre":
        octu += 1
    elif mes == "noviembre":
        nov += 1
    elif mes == "diciembre":
        dic += 1
    else:
        print("ERROR, Ingreso algun dato incorretco, vuelve a intenatrlo")
    total_edades += edad
prom_edades = total_edades / n_personas
print("La cantidad de estudiantes que cumplen años en enero son: ", enero)
print("La cantidad de estudiantes que cumplen años en febrero son: ", febrero)
print("La cantidad de estudiantes que cumplen años en marzo son: ", marzo)
print("La cantidad de estudiantes que cumplen años en abril son: ", abril)
print("La cantidad de estudiantes que cumplen años en mayo son: ", mayo)
print("La cantidad de estudiantes que cumplen años en junio son: ", junio)
print("La cantidad de estudiantes que cumplen años en julio son: ", julio)
print("La cantidad de estudiantes que cumplen años en agosto son: ", agosto)
print("La cantidad de estudiantes que cumplen años en septiembre son: ", sep)
print("La cantidad de estudiantes que cumplen años en octubre son: ", octu)
print("La cantidad de estudiantes que cumplen años en noviembre son: ", nov)
print("La cantidad de estudiantes que cumplen años en diciembre son: ", dic)

print("El promedio de edades es de: " ,prom_edades)
