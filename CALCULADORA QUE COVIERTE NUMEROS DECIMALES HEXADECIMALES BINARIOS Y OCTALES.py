def convertir_numero(numero, base_origen, base_destino):
    # Convertir el número a base 10
    if base_origen == 'decimal':
        num_base10 = int(numero)
    elif base_origen == 'binario':
        num_base10 = int(numero, 2)
    elif base_origen == 'octal':
        num_base10 = int(numero, 8)
    elif base_origen == 'hexadecimal':
        num_base10 = int(numero, 16)
    else:
        raise ValueError("Base de origen no válida.")

    # Convertir de base 10 a la base destino
    if base_destino == 'decimal':
        return str(num_base10)
    elif base_destino == 'binario':
        return bin(num_base10)[2:]
    elif base_destino == 'octal':
        return oct(num_base10)[2:]
    elif base_destino == 'hexadecimal':
        return hex(num_base10)[2:]
    else:
        raise ValueError("Base de destino no válida.")

def menu():
    print("Calculadora de conversión de bases")
    print("Bases disponibles: decimal, binario, octal, hexadecimal")
    numero = input("Ingrese el número a convertir: ")
    base_origen = input("Base de origen: ").lower()
    base_destino = input("Base de destino: ").lower()
    try:
        resultado = convertir_numero(numero, base_origen, base_destino)
        print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    menu()