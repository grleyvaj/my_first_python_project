# tuplas
tupla = (1, 2, 3, 4) # se definen con parentesis
# las tuplas son inmutables no es posible hacer tupla[0] = 5, mientras q las listas si lo son
lista = [1, 2, 3, 4]  # se definen con corchetes
lista[0] = 5
print(lista)

CONST = 4
# condicionales
print(CONST in lista)
print(CONST in tupla)
print("############################################")

# conocer la longitud
size = len(tupla)
print(size)

size = len(lista)
print(size)
print("############################################")

# conocer el indice de un elemento
inidice = tupla.index(3)
print(inidice)
print("############################################")

# ocurrencia de un elemento
tupla = (2, 1, 2, 3, 2, 6, 7, 2, 2, 2)
count = tupla.count(2)
print(count)
print("############################################")
