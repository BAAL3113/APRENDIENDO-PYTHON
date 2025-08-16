# Imprimir en pantalla
print("Hola, mundo!")  # Muestra el texto en la consola

# Asignar valores a variables
x = 5  # Asigna el valor 5 a la variable x

# Operaciones matemáticas
suma = 2 + 3  # Suma dos números
resta = 5 - 2  # Resta dos números
multiplicacion = 4 * 3  # Multiplica dos números
division = 10 / 2  # Divide dos números

# Estructura condicional
if x > 3:
    print("x es mayor que 3")  # Verifica si x es mayor que 3

# Bucle for
for i in range(5):
    print(i)  # Imprime los números del 0 al 4

# Bucle while
contador = 0
while contador < 3:
    print("Contador:", contador)  # Imprime el valor del contador
    contador += 1  # Incrementa el contador

# Definir una función
def saludar(nombre):
    print("Hola,", nombre)  # Saluda a la persona con el nombre dado

# Llamar a una función
saludar("Ana")  # Llama a la función saludar con el argumento "Ana"

# Crear una lista
frutas = ["manzana", "banana", "naranja"]  # Lista de frutas

# Acceder a elementos de una lista
print(frutas[0])  # Imprime el primer elemento de la lista

# Agregar elementos a una lista
frutas.append("pera")  # Agrega "pera" a la lista

# Diccionario
persona = {"nombre": "Juan", "edad": 30}  # Diccionario con datos de una persona

# Acceder a valores de un diccionario
print(persona["nombre"])  # Imprime el nombre de la persona

# Importar un módulo
import math  # Importa el módulo math

# Usar una función de un módulo
print(math.sqrt(16))  # Imprime la raíz cuadrada de 16

# Leer datos desde teclado
nombre = input("¿Cómo te llamas? ")  # Solicita al usuario su nombre
print("Bienvenido,", nombre)  # Saluda al usuario

# Manejo de excepciones (errores)
try:
    numero = int(input("Introduce un número entero: "))  # Intenta convertir la entrada a entero
    print("El doble es:", numero * 2)
except ValueError:
    print("¡Eso no es un número entero!")  # Mensaje si ocurre un error

# Uso de listas por comprensión (list comprehensions)
cuadrados = [i**2 for i in range(5)]  # Crea una lista con los cuadrados de 0 a 4
print("Cuadrados:", cuadrados)

# Uso de tuplas
coordenada = (10, 20)  # Tupla con dos valores
print("X:", coordenada[0], "Y:", coordenada[1])  # Imprime los valores de la tupla

# Uso de conjuntos (sets)
numeros = {1, 2, 3, 2, 1}  # Crea un conjunto (no permite duplicados)
print("Conjunto:", numeros)

# Función lambda (función anónima)
doble = lambda x: x * 2  # Define una función que duplica el valor
print("Doble de 7:", doble(7))

# Uso de f-strings para formatear texto
edad = 25
print(f"Tu edad es {edad} años")  # Imprime la edad usando f-string

# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")  # Imprime cada clave y valor del diccionario

# Uso de enumerate para obtener índice y valor en un bucle
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")  # Imprime el índice y la fruta

# Uso de zip para recorrer dos listas a la vez
colores = ["rojo", "verde", "azul"]
for fruta, color in zip(frutas, colores):
    print(f"{fruta} es de color {color}")  # Relaciona cada fruta con un color

# Uso de la función map para aplicar una función a cada elemento de una lista
numeros = [1, 2, 3, 4]
doblados = list(map(lambda x: x * 2, numeros))  # Duplica cada número de la lista
print("Números doblados:", doblados)

# Uso de la función filter para filtrar elementos de una lista
pares = list(filter(lambda x: x % 2 == 0, numeros))  # Filtra los números pares
print("Números pares:", pares)

# Uso de la función sorted para ordenar una lista
desordenados = [3, 1, 4, 2]
ordenados = sorted(desordenados)  # Ordena la lista
print("Lista ordenada:", ordenados)

# Uso de la función sum para sumar elementos de una lista
total = sum(numeros)  # Suma todos los números de la lista
print("Suma total:", total)

# Uso de la función range con paso personalizado
for i in range(0, 10, 2):
    print("Número par:", i)  # Imprime los números pares del 0 al 8

# Uso de la función len para obtener la longitud de una lista o cadena
print("Cantidad de frutas:", len(frutas))  # Imprime la cantidad de elementos en la lista

# Uso de la función type para saber el tipo de una variable
print("Tipo de variable 'x':", type(x))  # Imprime el tipo de la variable x

# Uso de la función help para obtener ayuda sobre funciones o módulos
# help(print)  # Descomenta esta línea para ver la ayuda de la función print en la consola