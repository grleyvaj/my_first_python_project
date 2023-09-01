# el valor de i se actualiza automaticamente, controlando el numero de elementos
for i in range(4):
    print(i)
print("############################################")

# definiento start, stop, step
for i in range(10, 20, 2):
    print(i)
print("############################################")

# ciclos sobre iterables, uno a la vez
numbers = [50, 40, 5, 2]
## con lista
for num in numbers:
    print(num)
print("############################################")
## con cadena d text
for char in "Loops":
    print(char)
print("############################################")
## con mapa
letras = {
    "a": 1,
    "b": 2,
}

# recorrer por claves
for clave in letras:
    print(f"La clave es: {clave}")
    print(f"El valor es: {letras[clave]}")
print("############################################")

# recorrer por los values
for valor in letras.values():
    print(f"El valor es: {valor}")
print("############################################")

# recorrer por clave y valor a la vez
for clave, valor in letras.items():
    print(clave, valor)
