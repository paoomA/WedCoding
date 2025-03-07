# Crear una matriz 3D para almacenar las temperaturas
# La estructura es: [ciudad][día de la semana][semana]
temperaturas = [
    [  # Ciudad: Machala
        [24, 23, 22],  # Semana 1: Lunes, Martes, Miércoles
        [23, 22, 21],  # Semana 2: Lunes, Martes, Miércoles
        [22, 21, 20]   # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Ciudad: Cuenca
        [18, 19, 20],  # Semana 1: Lunes, Martes, Miércoles
        [17, 18, 19],  # Semana 2: Lunes, Martes, Miércoles
        [21, 22, 23]   # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Ciudad: Portoviejo
        [30, 29, 28],  # Semana 1: Lunes, Martes, Miércoles
        [29, 28, 27],  # Semana 2: Lunes, Martes, Miércoles
        [32, 31, 30]   # Semana 3: Lunes, Martes, Miércoles
    ]
]

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(matriz, ciudades):
    for ciudad in range(len(matriz)):  # Iterar sobre las ciudades
        print(f"Promedios para la ciudad de {ciudades[ciudad]}:")
        for semana in range(len(matriz[ciudad])):  # Iterar sobre las semanas
            suma_temperaturas = sum(matriz[ciudad][semana])  # Sumar las temperaturas de los 3 días
            promedio = suma_temperaturas / len(matriz[ciudad][semana])  # Calcular el promedio
            print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")
        print("")  # Línea en blanco para separar las ciudades

# Nombres de las ciudades
ciudades = ["Machala", "Cuenca", "Portoviejo"]

# Llamar a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(temperaturas, ciudades)
