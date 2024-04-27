# Ejercicio 1

numeros = []
for i in range(4):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

maximo = numeros[0]
for num in numeros[1:]:
    if num > maximo:
        maximo = num

print("El número máximo es:", maximo)

# Ejercicio 2

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    maximo = num1
elif num2 >= num1 and num2 >= num3:
    maximo = num2
else:
    maximo = num3

if num1 <= num2 and num1 <= num3:
    minimo = num1
elif num2 <= num1 and num2 <= num3:
    minimo = num2
else:
    minimo = num3

intermedio = (num1 + num2 + num3) - maximo - minimo

print("Los números ordenados de forma descendente son:", maximo, intermedio, minimo)

# Ejercicio 3

anio = int(input("Ingrese su año de nacimiento: "))

if anio % 4 == 0:
    if anio % 100 != 0:
        print("Su año de nacimiento es en un año bisiesto.")
    elif anio % 400 == 0:
        print("Su año de nacimiento es en un año bisiesto.")
    else:
        print("Su año de nacimiento no es en un año bisiesto.")
else:
    print("Su año de nacimiento no es en un año bisiesto.")
