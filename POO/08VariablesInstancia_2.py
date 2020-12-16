class ClaseEjemplo:
    #Se han agregado dos guiones bajos a las propiedades.
    #Encapsulandolas y hacineodlas privadas.
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5

#El nombre _ClaseEjmplo_primera o demas, es completamente accesible fuera de la clase:

print(objetoEjemplo1._ClaseEjemplo__primera)
#No funcionara para una variable de instancia creada por fuera de la clase:

    #print(objetoEjemplo3._ClaseEjemplo__tercera)

#En este caso, se comportara como una propiedad ordinaria
print(objetoEjemplo3.__tercera)

print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)