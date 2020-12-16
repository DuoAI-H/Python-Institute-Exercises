class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "My name is " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)


#Como la clase Sub no tiene la funcion __str__ definida,
#obtenemos el nombre heredado de la superclase Super.
obj = Sub("Luis Pinto")

print(obj)