# funcion MAP

def doblar(numero):
    return numero * 2


numeros = [2, 5, 10, 23, 5, 33]

result = map(doblar, numeros)
print(result)
print(list(result))

print([x * 3 for x in numeros])
print([x * 3 for x in numeros])

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(list(map(lambda x, y: x * y, a, b)))
print("############################################")

enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)

print(cuadrados)
print("############################################")

# con mapas esto se haria asi
print([x ** 2 for x in enteros])
print([x ** 3 for x in enteros])

print("############################################")
# en lugar de enviar por parametro una lista de valores como segundo parametro pasamos una lista de funciones
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

funciones = [cuadrado, cubo]

for e in enteros:
    valores = [x(e) for x in funciones]
    print(valores)


print("############################################")
# funcion FILTER
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

print(pares)

# con filter
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x%2==0, valores))
print(pares)
print("############################################")

# funcion REDUCE usada para calculos acumulativos
valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el

print(suma)

# con reduce
from functools import reduce

suma = reduce(lambda x, y: x + y, valores)
print(suma)

print("############################################")

# mapa
lista_de_cadenas = ["5","6","7","8","9", "10"]
resultado = map(int,lista_de_cadenas) # en este caso la funcion ya existe, q es la d convertir a enteros -> int
print(list(resultado))
