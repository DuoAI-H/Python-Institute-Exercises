#Nota: El modificar una variable de instancia de cualquier objeto
#no tiene impacto en todos los objetos restantes

class ClaseEjemplo:
    def __init__(self, val = 1):
        #Variable de instancia creada por el constructor
        self.primera = val

    #Metodo set para poner valor a una varible
    #Metodo que crea una variable de instancia
    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
#Se ha enriquecido este objeto sobre la marcha
#Ahora tiene una propiedad llamada tercera
objetoEjemplo3.tercera = 5

#Cada objeto en Python viene con metodos y propiedades predefinidas
#como el objeto __dict__ (diccionario).

#La variable __dict__ contiene los nombres y valores de todas las propiedades
#que el objeto contiene actualmente.

print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)