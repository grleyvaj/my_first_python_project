num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

try:
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError as ex:
    print("Division por cero no permitida")
    print(ex)
except:
    print("Alerta, Hubo un error")
else:  # este else es para q el bloque se ejecute solo si no hubo excepciones, sino se pone, entonces el bloque se ejecuta despues de los prints q se hace en los catch
    print("Todo OK")
finally:  # es para un bloque q siempre se debe incluir
    print("Fin")

print("############################################")


# crear una excepcion propia
class LimiteDeKilometrosAlcanzadoError(Exception):
    pass
