#La manera de usarla es la siguiente:

    #assert expresion

#Hace lo siguiente:
#Evalua la expresion
#Si es True o cualquier valor diferente de 0 o None, no hara nada mas.
#Si no, generara una excepcion llamada AssertionError (La afirmacion ha fallado)

import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

#Genera una excepcion para valores negativos

x = math.sqrt(x)

print(x)

#Se usa para estar absolutamente a salvo de datos incorrectos.
#Cuando se usan funciones de otra persona.
