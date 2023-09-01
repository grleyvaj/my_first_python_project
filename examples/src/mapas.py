edades = {
    "Gino": 15,
    "Nora": 45,
}

# acceder al valor
print(edades["Gino"])
print("############################################")

# añadir al valor
print(edades)
edades["Talia"] = 67
print(edades)
print("############################################")

# si el valor asignado existe, se actualiza
edades["Talia"] = 50
print(edades)
print("############################################")

# eliminar valor del diccionario
del edades["Gino"]
print(edades)
print("############################################")

# revisar existencia
if "Gino" in edades:
    del edades["Gino"]
    print(edades)
print("############################################")
