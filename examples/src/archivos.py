# abrir el archivo
# al terminar se debe cerrar

# r indica el modo de apartura del archivo, r es modo d lectura
# r read
# w write
# a append-añadir
# aggregar un + incluye leer, ejemplo, w+ seria escribir y leer

# crear el archivo con la extension, en este caso .txt

# REEMPLAZAR completamente el text
with open("frases.txt", "w") as archivo:
    archivo.write("Dios te ama" + "\n")
archivo.close()

# LEER
with open("frases.txt") as archivo:
    for linea in archivo:
        print(" --- Frase --- ")
        print(linea)
archivo.close()

# AÑADIR
with open("frases.txt", "a") as archivo:
    archivo.write("Todo lo puedo en Cristo que me fortalece (Filipenses 4:13)" + "\n")
    archivo.write("Venid a mi todos los que estais trabajados y cargados y os hare descansar (Mateo 11:28)" + "\n")
archivo.close()

with open("frases.txt") as archivo:
    for linea in archivo:
        print(" --- Frase --- ")
        print(linea)
archivo.close()
print("############################################")

evaluaciones = {
    "Nora": 87,
    "Gino": 100,
    "Talina": 45,
}

with open("evaluaciones.txt", "w") as archivo:
    for nombre, nota in evaluaciones.items():
        archivo.write(nombre + "-" + str(nota) + "\n")
archivo.close()

with open("evaluaciones.txt") as archivo:
    for l in archivo:
        print(l)
archivo.close()
print("############################################")

mas_evaluaciones = {
    "Emily": 54,
    "Liam": 100,
}
with open("evaluaciones.txt", "a") as archivo:
    for nombre, nota in mas_evaluaciones.items():
        archivo.write(nombre + "-" + str(nota) + "\n")
archivo.close()

with open("evaluaciones.txt") as archivo:
    for l in archivo:
        print(l)
archivo.close()
