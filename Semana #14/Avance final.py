# Base de datos de clientes registrados
clientes_registrados = {"604890472": "Sebastian", "703110804": "Axel"}

# Definir las sedes y sus horarios
sedes = {
    "San José": {"horario": "24 horas, los 7 días de la semana.", "autos": ["Corolla", "Rav4", "Hilux", "Yaris"]},
    "Alajuela": {"horario": "24 horas, los 7 días de la semana.", "autos": ["Corolla", "Rav4", "Hilux", "Yaris"]},
    "Guanacaste": {"horario": "Abren a las 4 am, cierran a las 11 pm.", "autos": ["Corolla", "Hilux", "SantaFe", "Vitara"]},
    "Limón": {"horario": "Abren a las 6 am, cierran a las 10 pm.", "autos": ["Corolla", "Elantra", "Civic", "Swift"]},
    "Puntarenas": {"horario": "Abren a las 5 am, cierran a las 10 pm.", "autos": ["Corolla", "Rav4", "CR-V", "Pathfinder"]},
    "Pérez Zeledón": {"horario": "Abren a las 7 am, cierran a las 10 pm.", "autos": ["Corolla", "SantaFe", "Civic", "Vitara"]}
}

print("\nInicio de sesión:")
cedula = input("Ingrese su número de cédula o 'invitado' para continuar como invitado: ")

# Si el cliente no está registrado, solicitar detalles y registrar.
if cedula.lower() != 'invitado' and cedula not in clientes_registrados:
    nombre = input("Ingrese su Nombre: ")
    telefono = input("Ingrese su Número de Teléfono: ")
    clientes_registrados[cedula] = nombre
    print("Cliente {} registrado con éxito.".format(nombre))

print("Bienvenido,", clientes_registrados.get(cedula, "Invitado"))

# Si el cliente inicia sesión como invitado, mostrar solo la lista de autos disponibles.
if cedula.lower() == 'invitado':
    print("Lista de autos disponibles:")
    for sede, info in sedes.items():
        print(f"Sede: {sede}")
        print("Autos disponibles:")
        for auto in info["autos"]:
            print(auto)
        print()
else:
    pass

# Definir las variables del programa.
Toyota = str("Toyota")
Hyundai = str("Hyundai")
Honda = str("Honda")
Nissan = str("Nissan")
Suzuki = str("Suzuki")
name = str(input("Ingrese la marca del auto que desea reservar: "))
if name == Toyota:
    print("Toyota corolla: Quedan 4 disponibles.")
    print("Toyota Rav4: No disponibles por el momento.")
    print("Toyota Hilux: Quedan 3 disponibles.")
    print("Toyota Yaris: Quedan 2 disponibles.")
elif name == Hyundai:
    print("Hyundai Accent: No hay disponibles por el momento.")
    print("Hyundai Santa Fe: Quedan 2 disponibles.")
    print("Hyundai Elantra: Queda 1 disponible. ")
elif name == Honda:
     print("Honda Civic: Queda 3 disponible. ")
     print("Honda CR-V: Queda 2 disponible. ")
     print("Honda Accord: No hay disponible por el momento. ")
elif name == Nissan:
     print("Nissan Qashqai: Queda 3 disponible. ")
     print("Nissan Pathfinder: Queda 2 disponible. ")
     print("Nissan Sentra: No hay disponible por el momento. ")
elif name == Suzuki:
     print("Suzuki Vitara: Queda 2 disponible. ")
     print("Suzuki Swift: Queda 1 disponible. ")
     print("Suzuki Celerio : No hay disponible por el momento. ")
else:
    print("Disculpe, Desea elegir otro vehiculo")

# Definición de sedes y sus horarios
sedes = {
    "San José": {"horario": "24 horas, los 7 días de la semana.", "autos": ["Corolla", "Rav4", "Hilux", "Yaris"]},
    "Alajuela": {"horario": "24 horas, los 7 días de la semana.", "autos": ["Corolla", "Rav4", "Hilux", "Yaris"]},
    "Guanacaste": {"horario": "Abren a las 4 am, cierran a las 11 pm.", "autos": ["Corolla", "Hilux", "SantaFe", "Vitara"]},
    "Limón": {"horario": "Abren a las 6 am, cierran a las 10 pm.", "autos": ["Corolla", "Elantra", "Civic", "Swift"]},
    "Puntarenas": {"horario": "Abren a las 5 am, cierran a las 10 pm.", "autos": ["Corolla", "Rav4", "CR-V", "Pathfinder"]},
    "Pérez Zeledón": {"horario": "Abren a las 7 am, cierran a las 10 pm.", "autos": ["Corolla", "SantaFe", "Civic", "Vitara"]}
}
print("Disculpe, ¿desea cambiar de sede?")
cambio_sede = input("Ingrese 'si' para cambiar de sede o 'no' para continuar: ")
if cambio_sede.lower() == 'si':
    print("Sede 2: Dirección de la nueva sede")
    sede_nueva = input("Ingrese el nombre de la nueva sede: ")
    if sede_nueva in sedes:
        print("Sede:", sede_nueva)
        print("Horario:", sedes[sede_nueva]["horario"])
        print("Catálogo de autos disponibles en esta sede:")
        for auto in sedes[sede_nueva]["autos"]:
            print(auto)
    else:
        print("Disculpe, la sede seleccionada no está disponible.")
else:
    print("Continuamos con la selección de vehículo en la sede actual.")


# Elejir  el modelo del auto 
Corolla = str("Corolla")
Rav4 = str("Rav4")
Hilux = str("Hilux")
Yaris = str("Yaris")
# Aca termina los modelos de Toyota y empiezan los de Hyundai.
Accent = str("Accent")
SantaFe = str("SantaFe")
Elantra = str("Elantra")
# Aca termina los modelos de Hyundai y empiezan los de Honda.
Civic = str("Civic")
CR_V = str("CR-V")
Accord = str("Accord")
# Aca termina los modelos de Honda y empiezan los de Nissan.
Qashqai = str("Qashqai")
Pathfinder = str("Pathfinder")
Sentra = str("Sentra")
# Aca terminan los modelos de Nissan y empiezan los de Suzuki.
Vitara = str("Vitara")
Swift = str("Swift")
Celerio = str("Calerio")

modelo = str(input("Que modelo de auto desea reservar: "))
print("Elegiste el modelo", name, modelo)

if modelo == Corolla:
    print("Marca: Toyota | Año: 2017 | Cilindraje: 4 cilindros | Precio del vehículo: 7.000.000  | placa: MTZ-098 | Color: Gris ")
    print("Marca: Toyota | Año: 2020 | Cilindraje: 4 cilindros | Precio del vehículo: 11.000.000 | placa: QWR-908 | Color: Negro ")
    print("Marca: Toyota | Año: 2022 | Cilindraje: 4 cilindros | Precio del vehículo: 14.000.000 | placa: NPL-809 | Color: Blanco ")
    print("Marca: Toyota | Año: 2019 | Cilindraje: 4 cilindros | Precio del vehículo: 10.000.000 | placa: ZJK-980 | Color: Azul Marino")
elif modelo == Rav4:
    print("No disponible por el momento, ¿desea cambiar de Sede?")
elif modelo == Hilux:
     print("Marca: Toyota | Año: 2021 | Cilindraje: 4 cilindros | Precio del vehículo: 9.000.000  | placa: XZL-256 | Color: Rojo")
     print("Marca: Toyota | Año: 2022 | Cilindraje: 4 cilindros | Precio del vehículo: 13.000.000 | placa: HJG-625 | Color: blanco ")
     print("Marca: Toyota | Año: 2018 | Cilindraje: 4 cilindros | Precio del vehículo: 16.000.000 | placa: OQW-526 | Color: Negro ")
elif modelo == Yaris:
     print("Marca: Toyota | Año: 2016 | Cilindraje: 3 cilindros | Precio del vehículo: 7.000.000 | placa: KLV-801 | Color: Rojo ")
     print("Marca: Toyota | Año: 2020 | Cilindraje: 3 cilindros | Precio del vehículo: 5.000.000 | placa: VLK-108 | Color: Celeste") 
# Terminan los modelos de Toyota.
elif modelo == Accent:
     print("No disponible por el momento, ¿desea cambiar de Sede?")
elif modelo == SantaFe:
     print("Marca: Hyundai | Año: 2022 | Cilindraje: 4 cilindros | Precio del vehículo: 12.000.000 | placa: NBC-364  | Color: Rojo") 
     print("Marca: Hyundai | Año: 2019 | Cilindraje: 4 cilindros | Precio del vehículo: 9.000.000  |  placa: BCN-463 | Color: Gris ")
elif modelo == Elantra: 
      print("Marca: Hyundai | Año: 2018 | Cilindraje: 4 cilindros | Precio del vehículo: 10.000.000| placa: QML-048 | Color: Negro")
# Terminan los modelos de Hyundai.
elif modelo == Civic:
      print("Marca: Honda | Año: 2018 | Cilindraje: 4 cilindros | Precio del vehículo: 13.000.000 | placa: RJV-718 | Color: Rojo")
      print("Marca: Honda | Año: 2017 | Cilindraje: 4 cilindros | Precio del vehículo: 10.000.000 | placa: JVR-871 | Color: Verde Oscuro")
      print("Marca: Honda | Año: 2020 | Cilindraje: 4 cilindros | Precio del vehículo: 15.000.000 | placa: VRJ-178 | Color: Negro")
elif modelo == CR_V:
     print("Marca: Honda | Año: 2022 | Cilindraje: 4 cilindros | Precio del vehículo: 13.000.000 | placa: KJD-257  | Color: Gris")
     print("Marca: Honda | Año: 2018 | Cilindraje: 4 cilindros | Precio del vehículo: 11.000.000 | placa: DJK-752  | Color: Negro")
elif modelo == Accord:
     print("No disponible por el momento, ¿desea cambiar de Sede?")
# Terminan los modelos de Honda.
elif modelo == Qashqai:
     print("Marca: Nissan | Año: 2017 | Cilindraje: 4 cilindros | Precio del vehículo: 11.000.000 | placa: SWQ-912  | Color: Gris")
     print("Marca: Nisaan | Año: 2018 | Cilindraje: 4 cilindros | Precio del vehículo: 14.000.000 | placa: WQS-291  | Color: Blanco")
     print("Marca: Nissan | Año: 2021 | Cilindraje: 4 cilindros | Precio del vehículo: 17.000.000 | placa: QSW-192  | Color: Azul")
elif modelo == Pathfinder:
     print("Marca: Nissan | Año: 2017 | Cilindraje: 6 cilindros | Precio del vehículo: 13.000.000 | placa: ZXL-602  | Color: Blanco")
     print("Marca: Nissan | Año: 2020 | Cilindraje: 6 cilindros | Precio del vehículo: 16.000.000 | placa: LZX-206  | Color: Azul Oscuro")
elif modelo == Sentra:
     print("No disponible por el momento, ¿desea cambiar de Sede?")
# Terminan los modelos de Nissan.
elif modelo == Vitara:
     print("Marca: Suzuki | Año: 2017 | Cilindraje: 4 cilindros | Precio del vehículo: 9.000.000  | placa: FGH-320  | Color: Blanco")
     print("Marca: Suzuki | Año: 2020 | Cilindraje: 4 cilindros | Precio del vehículo: 12.000.000 | placa: HFG-032  | Color: Blanco")
elif modelo == Swift:
     print("Marca: Suzuki | Año: 2020 | Cilindraje: 4 cilindros | Precio del vehículo: 10.000.000 | placa: XMN-387  | Color: Blanco")
elif modelo == Celerio:
      print("No disponible por el momento, ¿desea cambiar de Sede?")

else:
    print("Disculpe, ¿desea cambiar de sede?")
cambio_sede = input("Ingrese 'si' para cambiar de sede o 'no' para continuar: ")
if cambio_sede.lower() == 'si':
    print("Sede 2: Dirección de la nueva sede")
    sede_nueva = input("Ingrese el nombre de la nueva sede: ")
    if sede_nueva in sedes:
        print("Sede:", sede_nueva)
        print("Horario:", sedes[sede_nueva]["horario"])
        print("Catálogo de autos disponibles en esta sede:")
        for auto in sedes[sede_nueva]["autos"]:
            print(auto)
    else:
        print("Disculpe, la sede seleccionada no está disponible.")
else:
    print("Continuamos con la selección de vehículo en la sede actual.")

reserva_exitosa = False

while not reserva_exitosa:
    modelo_reserva = input("¿Qué modelo de auto desea reservar?: ")
    año_reserva = input("¿Cuál sería el año del automóvil que quieres?: ")

    if modelo_reserva in sedes['San José']['autos']:
        autos_disponibles = sedes['San José']['autos']
        if modelo_reserva == "Corolla":
            if año_reserva == "2017":
                print("Has reservado un Toyota Corolla del año 2017.")
                reserva_exitosa = True
            elif año_reserva == "2019":
                print("Has reservado un Toyota Corolla del año 2019.")
                reserva_exitosa = True
            elif año_reserva == "2020":
                print("Has reservado un Toyota Corolla del año 2020.")
                reserva_exitosa = True
            elif año_reserva == "2022":
                print("Has reservado un Toyota Corolla del año 2022.")
                reserva_exitosa = True
            else:
                print("Lo sentimos, el automóvil de ese año no está disponible.")
        elif modelo_reserva == "Rav4":
            print("Lo sentimos, Toyota Rav4 no está disponible en la sede actual.")
            reserva_exitosa = True
        elif modelo_reserva == "Hilux":
            if año_reserva == "2018":
                print("Has reservado un Toyota Hilux del año 2018.")
                reserva_exitosa = True
            elif año_reserva == "2021":
                print("Has reservado un Toyota Hilux del año 2021.")
                reserva_exitosa = True
            elif año_reserva == "2022":
                print("Has reservado un Toyota Hilux del año 2022.")
        elif modelo_reserva == "Yaris":
            if año_reserva == "2016":
                print("Has reservado un Toyota Yaris del año 2016.")
                reserva_exitosa = True
            elif año_reserva == "2020":
                print("Has reservado un Toyota Yaris del año 2020.")
                reserva_exitosa = True
    if modelo_reserva == "SantaFe":
        if año_reserva == "2022":
                    print("Has reservado un Hyundai Santafe del año 2022.")
                    reserva_exitosa = True
        elif año_reserva == "2019":
                print("Has reservado un Hyundai SantaFe del año 2019.")
    if modelo_reserva == "Elantra":
        if año_reserva == "2018":
                    print("Has reservado un Hyundai Elantra del año 2018.")
                    reserva_exitosa = True
            # Agregar más condiciones para otros modelos y años disponibles si es necesario
    if modelo_reserva == "Civic":
        if año_reserva == "2017":
                    print("Has reservado un Honda Civic del año 2017.")
                    reserva_exitosa = True
        elif año_reserva == "2018":
                print("Has reservado un Honda Civic del año 2018.")
                reserva_exitosa = True
        elif año_reserva == "2020":
            print("Has reservado un Honda Civic del año 2020.")
            reserva_exitosa = True
    if modelo_reserva == "CR_V":
        if año_reserva == "2022":
                    print("Has reservado un Honda CR_V del año 2022.")
                    reserva_exitosa = True
        elif año_reserva == "2018":
            print("Has reservado un Honda CR_V del año 2018.")
            reserva_exitosa = True
        elif modelo_reserva == "Accord":
            print("Lo sentimos, Honda Accord no está disponible en la sede actual.")
            reserva_exitosa = True 
    if modelo_reserva == "Qashqai":
        if año_reserva == "2017":
                    print("Has reservado un Nissan Qashqai del año 2017.")
                    reserva_exitosa = True
        elif año_reserva == "2018":
                print("Has reservado un  Nissan Qashqai del año 2018.")
                reserva_exitosa = True
        elif año_reserva == "2021":
                print("Has reservado un  Nissan Qashqai del año 2021.")
                reserva_exitosa = True
    if modelo_reserva == "Pathfinder":
        if año_reserva == "2017":
            print("Has reservado un Nissan Pathfinder del año 2017.")
            reserva_exitosa = True
        elif año_reserva == "2020":
                print("Has reservado un  Nissan Pathfinder del año 2020.")
                reserva_exitosa = True
        elif modelo_reserva == "Sentra":
            print("Lo sentimos, Nissan Sentra no está disponible en la sede actual.")
            reserva_exitosa = True
    if modelo_reserva == "Vitara":
        if año_reserva == "2017":
            print("Has reservado un Suzuki Vitara del año 2017.")
            reserva_exitosa = True
        elif año_reserva == "2020":
                print("Has reservado un Suzuki Vitara del año 2020.")
                reserva_exitosa = True
    if modelo_reserva == "Swift":
        if año_reserva == "2020":
            print("Has reservado un Suzuki Swift del año 2020.")
            reserva_exitosa = True
        elif modelo_reserva == "Celerio":
            print("Lo sentimos, Suzuki Celerio no está disponible en la sede actual.")
            reserva_exitosa = True
        else:
            print("Lo sentimos, el modelo ingresado no está disponible en nuestra base de datos para la marca seleccionada.")     

import os

archivo_practica = "practica_progra.txt"

while True:
    print("Bienvenido a la gestion de reservas de FideRents")
    accion = int(input("Para llevar una gestion de reserva mas ordenada por favor digite 1 para ingresar el nombre y el auto que reservo , 2 para ver todas las reservas o 3 para salir: "))
    
    if accion == 1:
        montos = input("Para llevar un control de su eleccion, digite su nombre y el Auto que reservo porfavor: ")
        with open(archivo_practica, "a") as archivo:
            archivo.write(montos + "\n")
    elif accion == 2:
        with open(archivo_practica, "r") as archivo:
            print("Nombre y autos registrados:")
            for linea in archivo:
                print(linea.strip())
    elif accion == 3:
        print("Gracias por utilizar este programa")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
