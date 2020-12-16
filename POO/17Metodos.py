#Nota: la propiedad __name__ contiene el nombre de la clase.
#Esta ausente del objeto, es solo accesible para la clase.
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
#La funcion type() es capaz de encontrar una clase que haya instanciado el objeto.
print(type(obj).__name__)