#Ejercicio 1 ciclista
dias = ["lunes", "martes","miercoles","jueves","viernes","sabado","domingo"]
kilometros_por_dia = [0]*7

for dia in range(7):
    kilometros = float(input(f"Cuantos kilometros recorrio el dia {dias[dia]}:"))
    kilometros_por_dia[dia] = kilometros

total_de_semana = 0 
for dia in range(7):
    total_de_semana += kilometros_por_dia[dia]
    print(f"Dia {dias[dia]}:",kilometros_por_dia[dia], "kilometros")
print("Total de kilometros recorridos en la semana :", total_de_semana ,"kilometros")

#Ejercicio 2 butacas

fila_teatro = [''] * 10

for _ in range(10):
    nombre = input("Ingrese el nombre del ocupante: ")
    posicion = int(input("Ingrese el numero de butaca: "))
    
    if fila_teatro[posicion - 1] == '':
        fila_teatro[posicion - 1] = nombre
        print("Butaca asignada correctamente.")
    else:
        print("La butaca ya esta ocupada.")

print("Fila del teatro:")
for i in range(10):
    print("Butaca", i + 1, ":", fila_teatro[i])

# ejercicio 3 palabra al reves 

def revertir_palabra(palabra):
    palabra_al_reves = palabra[::-1]
    return palabra_al_reves

palabra = input("Ingrese una palabra: ")
print("La palabra al reves es:", revertir_palabra(palabra))

# ejercicio 4 salario

dias_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
monto_por_dia = ()

for dia in dias_semana:
    monto = float(input("Ingrese el monto ganado el " + dia + ": "))
    monto_por_dia += (monto,)

total_semana = 0
for monto in monto_por_dia:
    total_semana += monto

dia_menos_ganancia = dias_semana[0]
menor_ganancia = monto_por_dia[0]
for i in range(1, len(monto_por_dia)):
    if monto_por_dia[i] < menor_ganancia:
        menor_ganancia = monto_por_dia[i]
        dia_menos_ganancia = dias_semana[i]

print("Total ganado en la semana:", total_semana)
print("El dia que gano menos dinero fue el", dia_menos_ganancia, "con", menor_ganancia, "de ganancia.")



