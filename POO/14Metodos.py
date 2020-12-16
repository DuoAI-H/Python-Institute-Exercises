class conClase:
    #Los constructores y metodos se comportan como funciones ordinarias.
    #Aca se le asigna un valor predeterminado.
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)