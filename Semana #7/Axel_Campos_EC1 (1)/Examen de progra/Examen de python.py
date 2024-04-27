# Rifa de Semana 1
 
numero_ganador = 76
print("Bienvenidos a la reunion de la rifa de la semana 1")

premio_1 = 500
premio_2 = 1000
premio_3 = 2000
premio_4 = 5000
total_monto = 0
n_personas = int(input("Ingrese la cantidad de personas que asistieron a la reunion: "))

ganador_encontrado = False

for i in range(n_personas):
    nombre = input("Ingresar su nombre: ")
    cedula = input("Ingresar su cedula: ")
    monto = int(input("Ingresar el monto que va a donar: "))
    numero_rifa = int(input("Ingresar su numero de rifa: "))

    if numero_rifa == numero_ganador:
        ganador_encontrado = True
        premio = ""
        if monto == premio_1:
            premio = "hamburguesa con papas y gaseosa"
        elif monto == premio_2:
            premio = "Cupon cena para dos personas"
        elif monto == premio_3:
            premio = "un dia en el parque de diversiones con transporte y comida para tres personas"
        elif monto == premio_4:
            premio = "fin de semana"
        print("Felicidades, " + nombre + " ha ganado con el numero " + str(numero_rifa) + " y su premio es: " + premio)

if not ganador_encontrado:
    print("No se encuentra ningun ganador para el numero", numero_ganador)
total_monto += monto
prom_montos = total_monto / n_personas
print("El promedio de montos es de: " ,prom_montos)
# Rifa de Semana 2

numero_ganador_2 = 12
print("Bienvenido a la reunion de la rifa de la semana 2")

premio_1 = 500
premio_2 = 1000
premio_3 = 2000
premio_4 = 5000
total_monto = 0

n_personas = int(input("Ingrese la cantidad de personas que asistieron a la reunion: "))

ganador_encontrado = False

for i in range(n_personas):
    nombre_2 = input("Ingresar su nombre: ")
    cedula_2 = input("Ingresar su cedula: ")
    monto_2 = int(input("Ingresar el monto que va a donar: "))
    numero_rifa_2 = int(input("Ingresar su numero de rifa: "))

    if numero_rifa_2 == numero_ganador_2:
        ganador_encontrado = True
        premio = ""
        if monto == premio_1:
            premio = "hamburguesa con papas y gaseosa"
        elif monto == premio_2:
            premio = "Cupon cena para dos personas"
        elif monto == premio_3:
            premio = "un dia en el parque de diversiones con transporte y comida para tres personas"
        elif monto == premio_4:
            premio = "fin de semana"
        print("Felicidades, " + nombre_2 + " ha ganado con el numero " + str(numero_rifa_2) + " y su premio es: " + premio)

if not ganador_encontrado:
    print("No se encontro ningun ganador para el numero", numero_ganador_2)

total_monto += monto
prom_montos = total_monto / n_personas
print("El promedio de montos es de: " ,prom_montos)

# Rifa de Semana 3

numero_ganador_3 = 28
print("Bienvenido a la reunion de la rifa de la semana 3")

premio_1 = 500
premio_2 = 1000
premio_3 = 2000
premio_4 = 5000
total_monto = 0

n_personas = int(input("Ingrese la cantidad de personas que asistieron a la reunion: "))

ganador_encontrado = False

for i in range(n_personas):
    nombre_3 = input("Ingresar su nombre: ")
    cedula_3 = input("Ingresar su cedula: ")
    monto_3 = int(input("Ingresar el monto que va a donar: "))
    numero_rifa_3 = int(input("Ingresar su numero de rifa: "))

    if numero_rifa_3 == numero_ganador_3:
        ganador_encontrado = True
        premio = ""
        if monto == premio_1:
            premio = "hamburguesa con papas y gaseosa"
        elif monto == premio_2:
            premio = "Cupon cena para dos personas"
        elif monto == premio_3:
            premio = "un dia en el parque de diversiones con transporte y comida para tres personas"
        elif monto == premio_4:
            premio = "fin de semana"
        print("Felicidades, " + nombre_3 + " ha ganado con el numero " + str(numero_rifa_3) + " y su premio es: " + premio)

if not ganador_encontrado:
    print("No se encontro ningun ganador para el numero", numero_ganador_3)

total_monto += monto
prom_montos = total_monto / n_personas
print("El promedio de montos es de: " ,prom_montos)

# Rifa de Semana 4

numero_ganador_4 = 4
print("Bienvenido a la reunion de la rifa de la semana 4")

premio_1 = 500
premio_2 = 1000
premio_3 = 2000
premio_4 = 5000
total_monto = 0

n_personas = int(input("Ingrese la cantidad de personas que asistieron a la reunion: "))

ganador_encontrado = False

for i in range(n_personas):
    nombre_4 = input("Ingresar su nombre: ")
    cedula_4 = input("Ingresar su cedula: ")
    monto_4 = int(input("Ingresar el monto que va a donar: "))
    numero_rifa_4 = int(input("Ingresar su numero de rifa: "))

    if numero_rifa_4 == numero_ganador_4:
        ganador_encontrado = True
        premio = ""
        if monto == premio_1:
            premio = "hamburguesa con papas y gaseosa"
        elif monto == premio_2:
            premio = "Cupon cena para dos personas"
        elif monto == premio_3:
            premio = "un dia en el parque de diversiones con transporte y comida para tres personas"
        elif monto == premio_4:
            premio = "fin de semana"
        print("Felicidades, " + nombre_4 + " ha ganado con el numero " + str(numero_rifa_4) + " y su premio es: " + premio)

if not ganador_encontrado:
    print("No se encontro ningun ganador para el numero", numero_ganador_4)

total_monto += monto
prom_montos = total_monto / n_personas
print("El promedio de montos es de: " ,prom_montos)
