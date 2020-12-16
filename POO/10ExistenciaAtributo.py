#Nota: es posible que no todos los objetos de la misma clase
#tengan el mismo conjunto de propiedades.

class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)

#Evita el problema de la propiedad inexistente

try:
    print(objetoEjemplo.a)
    print(objetoEjemplo.b)
except AttributeError:
    print('Hubo un error ')
except:
    pass