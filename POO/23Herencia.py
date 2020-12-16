#Nota: Python ofrece una funcion para indetificar una relacion entre dos clases y
#puede verificar si una clase particular es una subclase de otra clase.

    #issubclass(ClaseUno, ClaseDos)

#La funcion devuelve True si ClaseUno es subclase de ClaseDos.

class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass

#Cada clase se considera subclase de si misma.
for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()