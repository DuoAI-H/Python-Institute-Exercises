#Nota: Python busca componentes de objetos en el siguiente orden:
#1.Dentro del objeto mismo.
#2.En sus superclases, de abajo hacia arriba.
#3.Si hay mas de una clase en una ruta de herencia
class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha):
    pass


obj = Sub()

#Aca se puede ver como Python se conforma con la caracteristica
#de la entidad que se ajuste, cuando se repite, en este caso var y fun().
#Para el caso de las variables izq y der, logra saltar a la otra clase.
print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())