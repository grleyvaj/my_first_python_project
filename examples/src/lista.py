letras = ["b", "c"]
print(letras[0])
print("############################################")

# agregar elemento al final
letras.append("d")
print(letras)
print("############################################")

# agregar elemento en x posicion
letras.insert(0, "a")
print(letras)
print("############################################")

# eliminar 1ra ocurencia encontrada
letras = ["a", "b", "a", "c"]
letras.remove("a")
print(letras)
print("############################################")

# para eliminar solo si el valor se sabe que esta sino daria error
if "z" in letras:
    letras.remove("z")
print(letras)
print("############################################")

letras = ["k", "j", "k", "l"]
print(letras)
# para eliminar todas las ocurrencias encontradas
while "k" in letras:
    letras.remove("k")
    print(letras)
print("############################################")

# conocer el indice de un elemento en la lista
letras = ["k", "j", "k", "l"]
position = letras.index("l")
print(position)
position = letras.index("k")
print(position)

# si se consulta el index y el elemento no esta daria error, por eso se debe preguntar antes si esta
if "z" in letras:
    position = letras.index("z")
    print(position)
print("############################################")

# metodos importantes d las listas -> count, extend, pop, reverse, sort
## saber cuantas veces se repite un elemento en una lista
letras = ["k", "j", "k", "l"]
print(letras)
cant = letras.count("k")
print(cant)
while cant != 0:
    letras.remove("k")
    cant = cant - 1
    print(letras)
print("############################################")

## sumar listas
letras = ["k", "j", "k", "l"]
mas_letras = ["n", "o", "p", "k"]
letras.extend(mas_letras)
print(letras)
print("############################################")

## eliminar elemento en x posicion y lo retorna
letras = ["k", "j", "k", "l"]

print(letras)
eliminado = letras.pop(0)
print(letras)
print("eliminado el primero")
print(eliminado)

# si no especificas indice elimina el ultimo
print(letras)
print("eliminado el ultimo")
eliminado = letras.pop()
print(letras)
print(eliminado)
print("############################################")

# reversa el orden actual d la lista
print(letras)
letras.reverse()
print(letras)
print("############################################")

## ordena la lista
print(letras)
letras.sort()
print(letras)

