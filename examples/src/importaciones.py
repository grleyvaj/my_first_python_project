# modulos incorporados, como el math q tiene funciones matematicas

import math

result = math.pow(9, 2)
print(result)
print(math.pi) # acceder a una constante de un modulo e imprimirla

# importar modulos escritos
import modulo

modulo.restar(100, 3)

# usar nombres alternativos para los modulos
import modulo as math_util

math_util.restar(100,3)

# no es necesario importar el modulo completo, podemos indicar que elemento se usara
from math import pow

print(pow(9,2))
