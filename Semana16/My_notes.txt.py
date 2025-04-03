# Escritura del archivo usando write()
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales con mis gustos
    file.write("Nota 1: Mi nombre es Paola, y siempre busco formas de crear y disfrutar de la vida.\n")
    file.write("Nota 2: El arte es mi refugio, y la pintura me permite expresarme.\n")
    file.write("Nota 3: ¡Me encanta bailar! Las danzas son mi pasión.\n")

# Lectura del archivo usando readline()
with open("my_notes.txt", "r") as file:
    # Leemos una línea a la vez utilizando readline().
    line = file.readline()
    while line:  # Mientras haya una línea en el archivo
        print(line.strip())  # Usamos strip() para quitar los saltos de línea
        line = file.readline()  # Leemos la siguiente línea
