#Nota: las variables de clase es una propiedad en la que existe
#solo una copia y se almacena fuera de cualquier objeto.
class ClaseEjemplo:
    contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

#Las variables de clase no se muestran en el diccionario de un objeto:
#(Ya que las variables de clase no son parte del objeto).

#Una variable de clase siempre presenta el mismo valor en todos los objetos.

#Se puede intentar buscar la variable del mismo nombre, como se ve a continuacion:

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)