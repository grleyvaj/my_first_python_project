# cuadrado
# funcion tradicional
def cuadrado_func(x):
    return x * 2


print(cuadrado_func(3))

# funciones usando lambdas
def lambda_cuadrado_func(x):
    return x ** 2
print(lambda_cuadrado_func(3))

def lambda_cubo_func(x):
    return x ** 3
print(lambda_cubo_func(3))

def lambda_func(x):
    return x ** 2 >= 10
print(lambda_func(3))
print(lambda_func(5))

mi_dicc = {"A": 1, "B": 2, "C": 3}
def resto_por_3(x):
    return mi_dicc[x] % 3
print([(mi_dicc[x] % 3) for x in mi_dicc])

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrado = filter(lambda x: x % 2 != 0, mi_lista)
print(list(filtrado))

mi_dicc = {"A": 1, "B": 2, "C": 3}
print(sorted(mi_dicc, key=lambda x: mi_dicc[x]%3)) # Retorna ['C', 'A', 'B']

