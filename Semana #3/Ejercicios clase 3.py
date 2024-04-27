def mostrar_menu ():
    print("===Menú ===")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")


     
#Ejercicio 1
def accion1 ():
    print("Ejercicio 1")

    nombre=input("ingrese el nombre:")
    apellido_1=input("ingrese el primer apellido:")
    apellido_2=input("ingrese el segundo apellido:")
    
    mensaje_de_bienvenida = "bienvenido, estimado " + nombre +" "+ apellido_1 + " "+ apellido_2
    print(mensaje_de_bienvenida)

#Ejercicio 2
def accion2 ():
    print("Ejercicio 2")
    primer_numero = input("ingrese el primer numero:")
    segundo_numero = input("ingrese el segundo numero:")
    suma = int(primer_numero)+ int(segundo_numero)
    print(suma)
    resta = int(primer_numero) - int(segundo_numero)
    print(resta)
    multiplicacion = int(primer_numero) * int(segundo_numero)
    print(multiplicacion)
    division = int(primer_numero) / int(segundo_numero)
    print(division)

#Ejercicio 3
def accion3 ():
    print("Ejercicio 3")

    lado = input("ingrese la medida del lado del cuadrado:")
    lado = float(lado)

    area = lado ** 2
    perimetro = 4 * lado

    print("Area del cuadrado: " + str(area))
    print("Perimetro del cuadrado: " + str(perimetro))

#Ejercicio 4
def accion4 ():
    print("Ejercicio 4")

    edad_de_pedro = input("ingrese la edad de Pedro:")
    edad_de_luis = input("ingrese la edad de Luis:")
    print("La edad de Pedro es", edad_de_pedro)
    print("La edad de Luis es", edad_de_luis)
    print("Si Pedro tuviera la edad de Luis tendria:", edad_de_luis)
    print("si Luis tuviera la edad de Pedro tendria:", edad_de_pedro)

#Ejercicio 5
def accion5 ():
    print("Ejercicio 5")
    numero_1 = input("ingrese el numero a elevar:")
    numero_2 = input("ingrese el numero por el que se elevara:")
    resultado_1 = int(numero_1)**int(numero_2)
    print("El resultado de", numero_1 , "elevado a" , numero_2, "es" , resultado_1)

while True:

        mostrar_menu()

        seleccion = input("Seleccione una opción (1-5): ")

        if seleccion == "1":
            accion1()
        elif seleccion =="2":
            accion2 ()
        elif seleccion =="3":
            accion3 ()
        elif seleccion =="4":
            accion4 ()
        elif seleccion =="5":
            accion5 ()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
