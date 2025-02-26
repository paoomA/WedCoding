# Definir la matriz bidimensional 3x3 con valores numéricos
matriz = [
    [5, 8, 3],
    [1, 6, 9],
    [4, 7, 2]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_buscado:
                return f"El valor {valor_buscado} se encontró en la posición ({i}, {j})."
    return f"El valor {valor_buscado} no se encontró en la matriz."

# Solicitar al usuario el valor a buscar
valor = int(input("Ingrese el valor a buscar en la matriz: "))

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor)
print(resultado)