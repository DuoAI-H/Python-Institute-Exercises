class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

#Las variables del constructor solo estan contenidas en el objeto.
print(obj.__dict__)
#Mientras que las variables de clase estan contenidas en el objeto y la clase.
print(conClase.__dict__)