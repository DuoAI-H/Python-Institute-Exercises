class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  


#No estamos creando otra clase aparte
#Estamos creando una subclase que apunta a la superclase Pila
#Esta hereda todos los componentes de su clase padre

    #class SumarPila(Pila):
        #pass

class SumarPila(Pila):
    def __init__(self):
        #Paso obligatorio:
        #Invocar explicitamente al constructor de la superclase
        Pila.__init__(self)
        self.__sum = 0