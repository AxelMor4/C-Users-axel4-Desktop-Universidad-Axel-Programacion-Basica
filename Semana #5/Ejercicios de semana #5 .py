#Ejercicio de practica 1)
def main():
    print("NÚMEROS PARES ENTRE 20 Y 40 Y SU CUADRADO")
    for i in range(20, 41):
        if i % 2 == 0:
            print(f"El número {i} es par y su cuadrado es {i**2}")

if __name__ == "__main__":
    main()


#Ejercicio de practica 2)

def main():
    total_estudiantes = 0
    total_aprobados = 0
    total_desaprobados = 0
    nota_maxima = 0
    nota_minima = 101

    while True:
        nota = int(input("Ingrese la nota del alumno (-1 para salir): "))
        if nota == -1:
            break

        total_estudiantes += 1
        if nota >= 70:
            total_aprobados += 1
        else:
            total_desaprobados += 1

        if nota > nota_maxima:
            nota_maxima = nota

        if nota < nota_minima:
            nota_minima = nota

    print(f"Total de estudiantes: {total_estudiantes}")
    print(f"Aprobados: {total_aprobados}")
    print(f"Desaprobados: {total_desaprobados}")
    print(f"Nota máxima: {nota_maxima}")
    print(f"Nota mínima: {nota_minima}")

if __name__ == "__main__":
    main()
