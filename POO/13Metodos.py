#Nota: El constructo no puede retornar un valor,
#ademas, no se puede invocar desde el objeto o desde dentro de la clase.
class conClase:
    #El metodo __init__ no es un metodo, es el constructor

    #Puede tener otros parametros ademas de self.
    #Se usa para inicializar adecuadamente el objeto.
        #-Crea variables de instancia.
        #-Crea instancias de cualquier otro objeto.
    def __init__(self, valor):
        self.var = valor

obj1 = conClase("objeto")

print(obj1.var)