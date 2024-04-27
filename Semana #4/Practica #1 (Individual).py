t = str("triangulo")
c = str("cuadrado")
figura = str(input("Introduzca C para cuadrado y introduzca T para triangulo: "))
lado = int(input("Introduzca el valor de los lados: "))
base = int(input("Introduzca el valor de la base: "))
altura = int(input("Introduzca el valor de la altura: "))

if figura == "t":
    lado = lado * 3
    area = base * altura
    print("La medida del perimetro es la siguiente: ", lado)
    print("La medida del area es la siguiente: ", area)
elif figura == "c":
        lado_2 = lado * 4
        area_2 = lado * 2
        print("La medida del perimetro es la siguiente: ", lado_2)
        print("La medida del area es la siguiente: ", area_2)
else:
    print("Letra incorrecta, intente de nuevo con una letra valida.")
    
