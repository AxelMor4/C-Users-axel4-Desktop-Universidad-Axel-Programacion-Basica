#Ejercicio 1
tiempo_vuelta_total =0
tiempo_pits_total =0
for i in range(1, 11):
    tiempo_vuelta = float(input("Ingrese el tiempo de la vuelta " "y" " en segundos: "))
    tiempo_pits = float(input("Ingrese el tiempo en PITS en segundos: "))

    tiempo_vuelta_total += tiempo_vuelta
    tiempo_pits_total += tiempo_pits

promedio_vuelta = tiempo_vuelta / 10

promedio_pits = tiempo_pits / 10

porcentaje_pits_vs_vuelta = (tiempo_pits) / (tiempo_vuelta) * 100


print("Tiempo promedio por vuelta: " ,promedio_vuelta, " segundos")
print("Tiempo promedio por PITS: " ,promedio_pits, " segundos")
print("Porcentaje del tiempo PITS respecto al tiempo de recorrido de una vuelta: " ,porcentaje_pits_vs_vuelta)

#Ejercicio 2

h_1 = 0 
h_2 = 0 
h_3 = 0
h_4 = 0 
h_5 = 0 
suma_altura = 0

n_ninos = int(input("Ingrese la cantidad de ninos que va a registrar la estatura: "))

for i in range(n_ninos):
    h = int(input("Ingrese la estatura del nino: "))
    if h < 100:
        h_1 += 1
    elif h >= 100 and h <=  120:
        h_2 += 1
    elif h >= 121 and h <=  130:
        h_3+= 1
    elif h >= 131 and h <=  140:
        h_4 += 1
    elif h > 140:
        h_5 += 1
    suma_altura += h
prom = suma_altura / n_ninos
print("El promedio de estaturas es de: ", prom)
print("Cantidad de niños que miden menos de 100 cm: ", h_1,
      "\nCantidad de niños que miden entre 100 y 120 cm: ", h_2,
      "\nCantidad de niños que miden entre 121 y 130 cm: ", h_3,
      "\nCantidad de niños que miden entre 131 y 140 cm: ", h_4,
      "\nCantidad de niños que miden más de 140 cm: ", h_5)

#Ejercicio 3
n = int(input("Ingrese un numero: "))

divisibles = []
contador = 1

while len(divisibles) < 10:
    if contador % n == 0:
        divisibles.append(contador)
    contador +=1

print(f"Los primeros 10 numeros divisibles entre {n} son: {divisibles}")

#Ejercicio 4 
salario_objetivo = 500

dinero_necesario = 0

for i in range(15): 
    salario = float(input("ingrese el salario #{}: ".format(i+1)))

    if salario < salario_objetivo:
        dinero_necesario += salario_objetivo - salario

print("para que todo ganen $500 se nececitan ${:.2f}".format(dinero_necesario))
