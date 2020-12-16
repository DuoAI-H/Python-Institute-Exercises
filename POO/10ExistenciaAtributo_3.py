#Nota: la funcion hasattr se puede usar para verificar
#si una variable de clase esta disponible.

class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))
print()

class ClaseEjemplo2:
    a = 1
    def __init__(self):
        self.b = 2

objetoEjemplo = ClaseEjemplo2()

print(hasattr(objetoEjemplo, 'b'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo2, 'b'))
print(hasattr(ClaseEjemplo2, 'a'))