def agregar_estudiante(estudiantes):
    """Agregar un nuevo estudiante al diccionario."""
    nombre = input("Ingresa el nombre del estudiante: ")
    grupo = int(input("Ingresa el número de grupo del estudiante: "))
    nota = float(input("Ingresa la nota del estudiante: "))
    estudiantes[nombre] = (grupo, nota)

def mostrar_estudiantes(estudiantes):
    """Imprimir la información de todos los estudiantes en el diccionario."""
    print("\nLista de estudiantes:")
    for nombre, info in estudiantes.items():
        grupo, nota = info
        print(f"{nombre}: Grupo {grupo}, Nota {nota}")

def main():
    """Función principal que muestra el menú y llama a las funciones."""
    estudiantes = {}
    while True:
        print("\n1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        try:
            opcion = int(input("Ingresa una opción: "))
            if opcion == 1:
                agregar_estudiante(estudiantes)
            elif opcion == 2:
                mostrar_estudiantes(estudiantes)
            elif opcion == 3:
                break
            else:
                print("Opción inválida, intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa una opción válida.")

    with open("datos_estudiantes.txt", "w") as f:
        for nombre, info in estudiantes.items():
            grupo, nota = info
            f.write(f"{nombre},{grupo},{nota}\n")

if __name__ == "__main__":
    main()


