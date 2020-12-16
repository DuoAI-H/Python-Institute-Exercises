#Nota: la funcion super() se usa para invocar el constructor de la clase heredada
#sin tener que nombrarla, ademas, permite tener acceso a todos los recursos de la superclase.
class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)


obj = Sub("Andy")

print(obj)