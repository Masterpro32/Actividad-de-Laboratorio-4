# |----- MANEJO DE CADENAS Y ESTRUCTURAS EN PYTHON -----|

# Declarar una cadena de texto
texto = "Diego vive en Lima y estudia programacion"
print("Texto original:")
print(texto)

# Obtener una subcadena
subcadena = texto[0:6]
print("\nSubcadena:")
print(subcadena)

# Buscar una palabra especifica
posicion = texto.find("Lima")
print("\nPosicion de la palabra 'Lima':")
print(posicion)

# Reemplazar una palabra por otra
nuevo_texto = texto.replace("Lima", "Cajamarca")
print("\nTexto reemplazado:")
print(nuevo_texto)
