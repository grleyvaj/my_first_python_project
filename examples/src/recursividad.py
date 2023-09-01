# caso base, con condicion de parada, version mas pequeña
# caso recursivo


# funcion fibonacci
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print("############################################")


# funcion factorial
def factorial(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)  # ir al caso base


print(factorial(1))
print(factorial(2))
print(factorial(3))

print("############################################")
