#! /usr/bin/env python3

# ^^^^^
#indica al sistema operativo cómo ejecutar el contenido del archivo.

""" module.py - an example of Python module """

#print(__name__)

#Los usuarios de mi modulo pueden acceder a mis variables
#Si deseo que no las editen, llego a un acuerdo con el usuario
#Escribe doble guion bajo o guion bajo sencillo, antes del nombre de la variables

__counter = 0

def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prod1(list):
    global __counter
    __counter +=1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)