# Crear un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "Pricila Velasco",
    "edad": 35 ,
    "ciudad": "Nueva Loja",
    "profesion": "Ingeniera"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Manta"

# Agregar una nueva clave-valor (por ejemplo, "telefono" si no existe)
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0968359008"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final después de las modificaciones:")
print(informacion_personal)
