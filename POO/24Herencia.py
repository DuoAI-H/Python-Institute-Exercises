#Nota: la funcion -isinstance()- permite saber si un objeto 
#es una encarnacion de una clase.

    #isinstance(nombreObjeto, nombreClase)

#La funcion devuelve True si el objeto es una instancia de la calse.
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

#Ser instanciado por una clase significa que el objeto ha sido creado 
#con el contenido de una clase o superclase.

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for clase in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, clase), end="\t")
    print()