#Practica programada 3

productos = {
    "Articulos enlatados": ["Atun", "Coctel de frutas", "Frijoles", "Cerezas"],
    "Productos de limpieza": ["Cloro", "MR musculo", "Laba platos", "Jabón de baño"],
    "Carnes": ["Pavo", "Pulpo", "Chuleta aumada", "Chuleta corriente"],
    "Granos": ["Almedras", "Mani", "Lentejas", "Garbanzos"]
}

def mostrar_productos():
    print("Los productos disponibles son los siguientes:")
    for tipo, lista_productos in productos.items():
        print(f"{tipo}:")
        if not lista_productos:
            print("El producto no esta en ninguna de las categoria.")
        else:
            for i, producto in enumerate(lista_productos, start=1):
                print(f"Producto {i}: {producto}")
        print()

def agregar_producto():
    tipo = input("Ingresar la categoria del producto: ")
    producto = input("Ingresar el nombre del producto: ")
    if producto in productos[tipo]:
        print("¡El producto ya se encuentra en la lista!")
    else:
        productos[tipo].append(producto)
        print(f"¡Producto {producto} agregado!")
        mostrar_productos()

def eliminar_producto():
    tipo = input("Ingresar la categoria del producto: ")
    producto = input("Ingresar el nombre del producto: ")
    if producto in productos[tipo]:
        productos[tipo].remove(producto)
        print(f"¡Producto {producto} eliminado!")
        mostrar_productos()
    else:
        print("¡Este producto no está en la lista!")

def actualizar_producto():
    tipo = input("Ingresar la categoria del producto: ")
    producto_antiguo = input("Ingresar el nombre del producto que va a actualizar: ")
    producto_nuevo = input("Ingresar el nombre del nuevo producto: ")
    if producto_antiguo in productos[tipo]:
        productos[tipo] = [producto_nuevo if producto == producto_antiguo else producto for producto in productos[tipo]]
        print(f"¡Producto {producto_antiguo} actualizado a {producto_nuevo}!")
        mostrar_productos()
    else:
        print("¡Este producto no está en la lista!")

while True:
    opcion = input("Ingrese la accion que desea  realizar (Lista, Añadir, eliminar, actualizar, salir): ")

    if opcion == "Lista":
        mostrar_productos()

    elif opcion == "Añadir":
        agregar_producto()

    elif opcion == "eliminar":
        eliminar_producto()

    elif opcion == "actualizar":
        actualizar_producto()

    elif opcion == "salir":
        print("¡Hemos terminado adios, hasta pronto.!")
        break

    else:
        print("ERROR, opcion incorrecta.")

    continuar = input("¿Deseas realizar alguna otra cosa? (si/no): ")
    if continuar.lower() != "si":
        print("¡Gracias!")
        break
