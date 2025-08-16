def fibonacci(n):
    # Crea una lista vacía para almacenar la secuencia de Fibonacci
    sequence = []
    # Inicializa los dos primeros números de la secuencia
    a, b = 0, 1
    # Itera n veces para generar la secuencia
    for _ in range(n):
        sequence.append(a)  # Agrega el número actual a la lista
        a, b = b, a + b     # Actualiza los valores de 'a' y 'b' al siguiente par de Fibonacci
    return sequence         # Devuelve la lista con la secuencia generada

# Ejemplo de uso:
cantidad = int(input("¿Cuántos números de Fibonacci quieres ver? "))  # Solicita al usuario la cantidad de números
print(fibonacci(cantidad))  # Imprime la secuencia