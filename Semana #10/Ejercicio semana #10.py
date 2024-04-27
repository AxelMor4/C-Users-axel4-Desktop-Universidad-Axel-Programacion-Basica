#Ejercicio  2 
def obtener_calificaciones():
    calificaciones = []
    for i in range(5):
        print(f"Ingrese las calificaciones del estudiante {i+1}:")
        fila = []
        for j in range(4):
            calificacion = float(input(f"Actividad {j+1}: "))
            fila.append(calificacion)
        calificaciones.append(fila)
    return calificaciones

def calcular_calificacion_final(calificaciones):
    n_estudiantes = len(calificaciones)
    n_actividades = len(calificaciones[0])
    pesos = [0.2, 0.2, 0.3, 0.3]  # pesos para cada actividad
    calificaciones_finales = []
    for i in range(n_estudiantes):
        calificacion_final = 0
        for j in range(n_actividades):
            calificacion_final += calificaciones[i][j] * pesos[j]
        calificaciones_finales.append(calificacion_final)
    return calificaciones_finales

def main():
    calificaciones = obtener_calificaciones()
    calificaciones_finales = calcular_calificacion_final(calificaciones)
    print("\nCalificaciones finales:")
    for i in range(5):
        print(f"Estudiante {i+1}: {calificaciones_finales[i]:.2f}")

if __name__ == "__main__":
    main()

#Ejercicio  3

def inicializar_asientos():
    """Inicializar la matriz de asientos con 0s."""
    asientos = []
    for i in range(4):
        fila = [0] * 20
        asientos.append(fila)
    return asientos

def reservar_asiento(asientos):
    """Reservar un asiento reemplazando el 0 con un 1."""
    turno = int(input("Ingrese el número de turno (1-4): ")) - 1
    asiento = int(input("Ingrese el número de asiento (1-20): ")) - 1
    if asientos[turno][asiento] == 0:
        asientos[turno][asiento] = 1
        print("Asiento reservado exitosamente.")
    else:
        print("El asiento ya está reservado.")

def main():
    """Función principal que muestra el menú y llama a las funciones."""
    asientos = inicializar_asientos()
    while True:
        print("\n1. Reservar asiento")
        print("2. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            reservar_asiento(asientos)
        elif opcion == 2:
            break
        else:
            print("Opción inválida, inténtalo nuevamente.")

if __name__ == "__main__":
    main()
