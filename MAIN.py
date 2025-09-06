from FUNCION_FIBONACCI import fibonacci_hasta
from DICCIONARIO import personas
def main():
    print("Bienvenido al programa de consola")
    print("Secuencia de Fibonacci:")
    fibonacci_hasta(10)
    print("\nLista de personas:")
    for persona in personas:
        if persona["gusto_de_musica"] == "Rock" or persona["gusto_de_musica"] == "Reggaetón":
            print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Sexo: {persona['sexo']}, Gusto de música: {persona['gusto_de_musica']}")
            if persona["gusto_de_musica"] == "Rock": 
                print({persona["nombre"]}, "tiene buen gusto musical")
            elif persona["gusto_de_musica"]== "Reggaetón":
                print({persona["nombre"]}, "no sirves para nada")
    # Función lambda (función anónima)
    doble = lambda x: x * 2  # Define una función que duplica el valor
    print("Doble de 7:", doble(7))           
    numeros = {1, 2, 3, 2, 1}  # Crea un conjunto (no permite duplicados)
    print("Conjunto:", numeros)
    print ("Doble de 14:",doble(14))
    # Iterar sobre un diccionario
    for clave, valor in persona.items():
        print (f"{clave}: {valor}")  # Imprime cada clave y valor del diccionario
    # Crear una lista
    frutas = ["manzana", "banana", "naranja"]  # Lista de frutas
    # Uso de enumerate para obtener índice y valor en un bucle
    for indice, fruta in enumerate(frutas):
        print(f"Índice {indice}: {fruta}")  # Imprime el índice y la fruta
    for clave,valor in enumerate(persona.items()):
        print (f"{clave}: {valor}")
if __name__ == "__main__":
    main()
