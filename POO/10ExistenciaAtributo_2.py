class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

#Verifica con seguridad si algun objeto o clase
#tiene una propiedad especifica.

#Funcion hasattr, consiste en dos argumentos:
#1. La clase o el objeto que se verifica.
#2. El nombre de la propiedad cuya existencia se desea verificar

#Retorna True o False

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)