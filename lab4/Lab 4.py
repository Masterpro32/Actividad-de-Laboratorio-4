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

# Separar el texto en partes
palabras = texto.split()
print("\nTexto separado en palabras:")
print(palabras)

# Implementar 2 listas paralelas
nombres = ["Diego", "Harol", "Haziel", "Jeanpier"]
edades = [20, 25, 22, 19]
buscar_nombre = "Haziel"
print("\nBusqueda en listas paralelas:")
if buscar_nombre in nombres:
    indice = nombres.index(buscar_nombre)
    print("Nombre:", buscar_nombre)
    print("Edad:", edades[indice])
else:
    print("Persona no encontrada")

# Lista de diccionarios--victoria
usuarios = [
    {
        "nombre": "Diego",
        "email": "diego@gmail.com",
        "ciudad": "Lima"
    },
    {
        "nombre": "Harol",
        "email": "harol@gmail.com",
        "ciudad": "Cajamarca"
    },
    {
        "nombre": "Victoria",
        "email": "victoria@gmail.com",
        "ciudad": "Lima"
    }
]

# Buscar usuarios por ciudad
ciudad_buscar = "Lima"
print("\nUsuarios encontrados en", ciudad_buscar)
for usuario in usuarios:
    if usuario["ciudad"] == ciudad_buscar:
        print(usuario)
