# Matriz 3D para almacenar las temperaturas por ciudad, semana y día
temperaturas = [
    [  # Ciudad: Machala
        [24, 23, 22, 21],  # Semana 1: Lunes - Domingo
        [23, 22, 21, 20],  # Semana 2: Lunes - Domingo
        [22, 21, 20, 19],  # Semana 3: Lunes - Domingo
        [21, 20, 19, 18]  # Semana 4:  Lunes - Domingo
    ],
    [  # Ciudad: Cuenca
        [18, 19, 20, 21],  # Semana 1: Lunes - Domingo
        [17, 18, 19, 20],  # Semana 2: Lunes - Domingo
        [21, 22, 23, 24],  # Semana 3: Lunes - Domingo
        [19, 20, 21, 22]  # Semana 4: Lunes - Domingo
    ],
    [  # Ciudad: Portoviejo
        [30, 29, 28, 27],  # Semana 1: Lunes - Domingo
        [29, 28, 27, 26],  # Semana 2: Lunes - Domingo
        [32, 31, 30, 29],  # Semana 3: Lunes - Domingo
        [31, 30, 29, 28]  # Semana 4: Lunes - Domingo
    ]
]

# Función para calcular el promedio de temperaturas por ciudad
def calcular_promedio_total(matriz, ciudades):
    for ciudad in range(len(matriz)):  # Iterar sobre cada ciudad
        total_temperaturas = 0  # Acumulador de todas las temperaturas de la ciudad
        total_datos = 0  # Contador del total de datos registrados

        for semana in range(len(matriz[ciudad])):  # Iterar sobre cada semana
            total_temperaturas += sum(matriz[ciudad][semana])  # Sumar temperaturas
            total_datos += len(matriz[ciudad][semana])  # Contar datos

        promedio_total = total_temperaturas / total_datos  # Calcular promedio total
        print(f"Promedio total de temperatura en {ciudades[ciudad]}: {promedio_total:.2f}°C")

# Nombres de las ciudades
ciudades = ["Machala", "Cuenca", "Portoviejo"]

# Llamar a la función para calcular y mostrar los promedios
desarrollar_promedio_total = calcular_promedio_total(temperaturas, ciudades)
