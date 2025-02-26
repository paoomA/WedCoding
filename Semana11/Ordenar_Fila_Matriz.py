# Definir la matriz bidimensional 3x3 con valores numéricos
matriz = [
    [9, 4, 7],
    [3, 8, 5],
    [6, 1, 2]
]


# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila_a_ordenar):
    # Verificar que la fila sea válida
    if fila_a_ordenar < 0 or fila_a_ordenar >= len(matriz):
        print("El número de fila ingresado no es válido.")
        return

    # Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Aplicar Bubble Sort a la fila especificada
    fila = matriz[fila_a_ordenar]
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)


# Solicitar al usuario la fila a ordenar
fila = int(input("Ingrese el número de la fila a ordenar (0, 1 o 2): "))

# Llamar a la función para ordenar la fila
ordenar_fila(matriz, fila)