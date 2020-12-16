# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

#Podemos acceder tambien a las variables de instancia heredadas
#solamente no olvidar invocar el constructor de la superclase.
print(obj.subVar)
print(obj.supVar)