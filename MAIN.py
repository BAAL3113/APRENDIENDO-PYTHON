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
if __name__ == "__main__":
    main()
