class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
#Con punto pero sin parentesis al final
print(len(objetoPila.listaPila))

#Asi se hace que un atributo sea privado:

"""
class Pila:
    def __init__(self):
        self.__listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))
"""

#Esto lo hace innacesible (PRIVADO), si lo intentamos llamar como la manera anterior
#A esto se le conoce como encapsulamiento

#Esto nos envia el siguiente error:

    #AttributeError