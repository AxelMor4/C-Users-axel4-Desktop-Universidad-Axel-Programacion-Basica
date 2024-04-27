def mostrar_menu():
    print("=== Menú ===")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Salir")

# Ejercicio 1
def accion1():
    print("Ejercicio 1")
    a = input("ingrese el valor a:")
    b = input("ingrese el valor b:")
    c = input("ingrese el valor c:")
    d = input("ingrese el valor d:")
    print(d,c,b,a)

#Ejercicio 2
def accion2():
    print("Ejercicio 2")
    edad = input("ingrese la edad: ")
    edad= int(edad)
    suma = edad + 5
    print("Dentro de 5 anhos, tendra: ", suma)


#Ejercicio 3
def accion3():
    print("Ejercicio 3")
    a = input("ingrese el valor de a:")
    b = input("ingrese el valor de b:")
    a=int (a)
    b=int (b)
    result = ((a+b)*2)/ 3
    print(result)

#Ejercicio 4
def accion4():
    print("Ejercicio 4")
    a = input("igrese el valor a:")
    a = int (a)
    result_2 = (a)**2
    result_3 = (a)**3
    print(result_2)
    print(result_3)

#Ejercicio 5
def accion5():
    print("Ejercicio 5")
    b = input("ingrese el valor de Base:")
    b = int (b)
    a = input("ingrese el valor de Altura:")
    a = int (a)
    result_1 = (b) * (a) 
    result_2 = (b) + (a)*2
    print(result_1)
    print(result_2)

# Ejercicio 6
def accion6():
    print("Ejercicio 6")
    print("Sistema para calcular gastos de viaje")
    d = input("ingrese la distancia de la casa a la U:")
    d = int(d)
    c = input("ingrese el costo por kilometro:")
    c = int(c)
    dia = input("ingrese los dias que viaja a la U por Semana:")
    dia = int(dia)
    constante= int(15)
    result_1 = (((d*c)*dia)*2)*constante
    print("El gasto del cuatrimeste es de:", result_1)

# Ejercicio 7
def accion7():
    print("Ejercicio 7")
    a=input("ingrese la edad de a:")
    a=int(a)
    b=input("ingrese la edad de b:")
    b=int(b)
    c=input("ingrese la edad de c:")
    c=int(c)
    d=input("ingrese la edad de d:")
    d=int(d)
    e=input("ingrese la edad de e:")
    e=int(e)
    result_1=(a+b+c+d+e)/5
    print("La edad promedio es de:", result_1)

#Ejercicio 8
def accion8():
    print("Ejercicio 8")
    a=input("ingrese la cantidad de horas semanales trabajadas:")
    a=float(a)
    b=input("ingrese el precio que se le paga por hora:")
    b=float(b)
    result_1=(a*b)-0.105-0.05*4.2
    print("el salario mensual es de:", result_1)


#Ejercicio 9
def accion9():
    print("Ejercicio 9")
    a=input("ingresos mensuales:")
    a=float(a)
    b=input("ingrese sus gastos mensuales por alimentacion:")
    b=float(b)
    result_1=(b/a)*100
    result_2=100-result_1
    print("porcentaje del rubro alimenticio es de:", result_1,"%")
    print("porcentaje que queda disponible para otros rubros es de:", result_2,"%")
    
def salir():
    print('Saliendo')


while True:


    mostrar_menu()

    seleccion = input("Selecciona una opción (1-10): ")

    if seleccion == "1":
        accion1()
    elif seleccion == "2":
        accion2()
    elif seleccion == "3":
        accion3()
    elif seleccion == "4":
        accion4()
    elif seleccion == "5":
        accion5()
    elif seleccion == "6":
        accion6()
    elif seleccion == "7":
        accion7()
    elif seleccion == "8":
        accion8()
    elif seleccion == "9":
        accion9()
        
    elif seleccion == "10":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")



