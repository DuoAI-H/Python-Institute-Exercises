class Pila:
    #Constructor
    def __init__(self):
        self.__listaPila = []

    #Funcion de agregar
    def push(self, val):
        self.__listaPila.append(val)
    #Funcion de quitar
    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())