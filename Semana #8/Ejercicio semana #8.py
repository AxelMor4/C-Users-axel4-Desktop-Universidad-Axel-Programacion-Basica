def decimal_a_binario(numero_decimal):
    return bin(numero_decimal)[2:]  # Convierte a binario y quita el prefijo '0b'

def decimal_a_octal(numero_decimal):
    return oct(numero_decimal)[2:]  # Convierte a octal y quita el prefijo '0o'

def decimal_a_hexadecimal(numero_decimal):
    return hex(numero_decimal)[2:].upper()  # Convierte a hexadecimal y quita el prefijo '0x'

def convertir_a_base(numero_decimal, base):
    if base == 2:
        return decimal_a_binario(numero_decimal)
    elif base == 8:
        return decimal_a_octal(numero_decimal)
    elif base == 16:
        return decimal_a_hexadecimal(numero_decimal)
    else:
        return "Base no soportada"

# Ejemplo de uso:
valor_decimal = 123

# Conversión a binario (muestra el resultado)
valor_binario = decimal_a_binario(valor_decimal)
print(f"Binario: {valor_binario}")

# Conversión a octal (retorna el resultado)
valor_octal = decimal_a_octal(valor_decimal)
print(f"Octal: {valor_octal}")

# Conversión a hexadecimal (retorna el resultado)
valor_hexadecimal = decimal_a_hexadecimal(valor_decimal)
print(f"Hexadecimal: {valor_hexadecimal}")

# Conversión a una base específica usando la función `convertir_a_base`
base = 16
resultado = convertir_a_base(valor_decimal, base)
if resultado != "Base no soportada":
    print(f"Valor en base {base}: {resultado}")
else:
    print("Base no soportada")
