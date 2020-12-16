class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

#Python busca las entidades de arriba hacia abajo,
#esto permite que si existe una funcion o variables
#con el mismo nombre, como en este caso, Python se
#conforme con la primera que ha encontrado, en este
#caso: la clase Nivel2.

class Nivel3(Nivel2, Nivel1):
    pass

obj = Nivel3()

print(obj.var, obj.fun())