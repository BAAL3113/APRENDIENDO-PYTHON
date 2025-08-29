def fibonacci_hasta(n):
    """
    Imprime los primeros n números de la secuencia de Fibonacci.
    :param n: La cantidad de números de Fibonacci a mostrar.
    """
    a, b = 0, 1
    contador = 0  # Lleva la cuenta de cuántos números se han mostrado
    while contador < n:
        print(a, end=' ')
        a, b = b, a + b
        contador += 1  # Incrementa el contador en cada iteración
    print()

# Ejemplo de uso:
# fibonacci_hasta(10)