def convertir_numero(numero, base_origen, base_destino):
    """
    Convierte un número de una base a otra.
    :param numero: El número a convertir (como string).
    :param base_origen: La base original del número ('decimal', 'binario', 'octal', 'hexadecimal').
    :param base_destino: La base a la que se quiere convertir ('decimal', 'binario', 'octal', 'hexadecimal').
    :return: El número convertido como string.
    """
    # Convertir el número a base 10 (decimal) según la base de origen
    if base_origen == 'decimal':
        num_base10 = int(numero)  # Convierte el string a entero decimal
    elif base_origen == 'binario':
        num_base10 = int(numero, 2)  # Convierte el string binario a decimal
    elif base_origen == 'octal':
        num_base10 = int(numero, 8)  # Convierte el string octal a decimal
    elif base_origen == 'hexadecimal':
        num_base10 = int(numero, 16)  # Convierte el string hexadecimal a decimal
    else:
        raise ValueError("Base de origen no válida.")  # Error si la base no es reconocida

    # Convertir el número decimal a la base destino
    if base_destino == 'decimal':
        return str(num_base10)  # Devuelve el número como string decimal
    elif base_destino == 'binario':
        return bin(num_base10)[2:]  # Convierte a binario y elimina el prefijo '0b'
    elif base_destino == 'octal':
        return oct(num_base10)[2:]  # Convierte a octal y elimina el prefijo '0o'
    elif base_destino == 'hexadecimal':
        return hex(num_base10)[2:]  # Convierte a hexadecimal y elimina el prefijo '0x'
    else:
        raise ValueError("Base de destino no válida.")  # Error si la base destino no es reconocida

def menu():
    """
    Muestra el menú al usuario y gestiona la entrada y salida.
    """
    print("Calculadora de conversión de bases")
    print("Bases disponibles: decimal, binario, octal, hexadecimal")
    numero = input("Ingrese el número a convertir: ")  # Solicita el número
    base_origen = input("Base de origen: ").lower()    # Solicita la base de origen
    base_destino = input("Base de destino: ").lower()  # Solicita la base de destino
    try:
        resultado = convertir_numero(numero, base_origen, base_destino)  # Realiza la conversión
        print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}.")
    except Exception as e:
        print("Error:", e)  # Muestra el error si ocurre

if __name__ == "__main__":
    menu()  # Ejecuta el menú si el archivo se ejecuta directamente