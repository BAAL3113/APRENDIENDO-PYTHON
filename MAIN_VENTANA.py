import tkinter as tk  # Importa la biblioteca de interfaz gráfica

def saludar():
    # Función que se ejecuta al presionar el botón
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola, {nombre}!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de ejemplo")

# Crear widgets (elementos de la ventana)
etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()