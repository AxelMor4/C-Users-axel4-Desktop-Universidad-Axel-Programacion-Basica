lunes= 0
martes = 0
miercoles= 0
jueves= 0
viernes= 0 
sabado= 0
domingo= 0
max_temperatura = 0
min_temperatura = 100

total_temperatura = 0
n_personas = int(input("Ingrese la cantidad de personas que va a registrar la temperatura: "))

for i in range(n_personas):
    dia = input("Ingrese el dia que desea registrar: ")
    temperatura = int(input("Ingrese la temperatura que presenta(0-100):"))
    if temperatura > max_temperatura:
        max_temperatura = temperatura
    if not temperatura > min_temperatura:
        min_temperatura =  temperatura
    elif dia == "lunes":
        lunes += 1
    elif dia == "martes":
        martes += 1
    elif dia == "miercoles":
        miercoles += 1
    elif dia == "jueves":
        jueves += 1
    elif dia == "viernes":
        viernes += 1
    elif dia == "sabado":
        sabado += 1
    elif dia == "domingo":
        domingo += 1

    else:
        print("Salir del registro")
    total_temperatura += temperatura
prom_temperaturas = total_temperatura / n_personas
print("La temperatura más alta fue: ",max_temperatura )
print("La temperatura más baja fue: ",min_temperatura )

print("El promedio de temperaturas es de: " ,prom_temperaturas)
