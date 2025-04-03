# Creación y escritura en el archivo my_notes.txt

# Definimos el nombre del archivo que vamos a crear
file_name = "my_notes.txt"

# Abrimos el archivo en modo escritura ("w")
# Si el archivo no existe, se creará automáticamente
# Si existe, su contenido será sobrescrito
archivo_escritura = open(file_name, "w")

# Escribimos tres líneas de notas personales usando write()
# Cada write() escribe una línea, añadiendo \n para salto de línea
archivo_escritura.write("Nota 1: Recordar realizar el deber de programación.\n")  # Escribe la primera nota
archivo_escritura.write("Nota 2: Revisar la materia compartida en clase en la plataforma.\n")  # Escribe la segunda nota
archivo_escritura.write("Nota 3: Preparar el codigo y subirlo.\n")  # Escribe la tercera nota

# Cerramos el archivo después de escribir
# Esto libera recursos y asegura que los datos se guarden
archivo_escritura.close()

# Lectura del archivo línea por línea

# Abrimos el mismo archivo ahora en modo lectura ("r")
archivo_lectura = open(file_name, "r")

# Mostramos un mensaje indicando que comenzamos a leer
print("Leyendo el contenido de my_notes.txt línea por línea:")  # Mensaje informativo

# Leemos la primera línea
linea = archivo_lectura.readline()  # Lee la primera línea del archivo

# Usamos un while loop para leer hasta que no haya más líneas
while linea != "":  # Mientras la línea no esté vacía
    # Mostramos la línea leída, eliminando el salto de línea final con strip()
    print(linea.strip())  # Imprime la línea sin saltos de línea adicionales
    # Leemos la siguiente línea
    linea = archivo_lectura.readline()  # Lee la siguiente línea del archivo

# Cerramos el archivo después de leer
archivo_lectura.close()  # Libera los recursos del sistema
