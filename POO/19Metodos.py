#Nota: __bases__ es una tupla que contiene clases,
#que son superclases directas para la clase.

#Ojo: No son nombres de clases, son clases.

class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass

#Solo las clases tienen el atributo __bases__

def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

#Una clase sin superclases apunta al objeto (clase de Python predefinida).
printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)