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
print(fibonacci(cantidad))  # Imprime la secuencia generada

#EJERCICIO 2 EN PYTHON
def es_primo(num):
    if num <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Si es divisible por algún número, no es primo
    return True  # Si no es divisible por ningún número, es primo

#EJERCICIO 3 EN PYTHON
def es_palindromo(texto):
    texto = texto.lower()  # Convierte el texto a minúsculas
    texto = ''.join(c for c in texto if c.isalnum())  # Elimina caracteres no alfanuméricos
    return texto == texto[::-1]  # Compara el texto con su reverso
# Ejemplo de uso:
frase = input("Introduce una frase para verificar si es un palíndromo: ")   
print("Es palíndromo." if es_palindromo(frase) else "No es palíndromo.")  # Imprime el resultado de la verificación
#EJERCICIO 4 EN PYTHON
def contar_vocales(texto):
    texto = texto.lower()  # Convierte el texto a minúsculas
    contador = 0  # Inicializa el contador de vocales
    for char in texto:
        if char in 'aeiouáéíóú':  # Verifica si el carácter es una vocal
            contador += 1  # Incrementa el contador si es una vocal
    return contador  # Devuelve el total de vocales encontradas 
# Ejemplo de uso:
frase = input("Introduce una frase para contar las vocales: ")  # Solicita al usuario una frase
print(f"Total de vocales: {contar_vocales(frase)}") 
#EJERCICIO 5 EN PYTHON
def calcular_factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."  # Maneja el caso de números negativos
    factorial = 1  # Inicializa el resultado del factorial
    for i in range(2, n + 1):  # Itera desde 2 hasta n
        factorial *= i  # Multiplica el resultado por cada número en el rango
    return factorial  # Devuelve el resultado del factorial 
# Ejemplo de uso:
numero = int(input("Introduce un número para calcular su factorial: "))  # Solicita al usuario un número
print(f"El factorial de {numero} es: {calcular_factorial(numero)}")