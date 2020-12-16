from sys import path

path.append('c:\\Users\\lfpin\\OneDrive\\Documentos\\VS Code\\Python\\Python Institute\\Intermedio\\Paquetes')

import extra.iota

print(extra.iota.FunI())

###

#O tambien se puede:

    #from extra.iota import FunI()
    #print(FunI())

###

#Ahora vamos hasta el final del arbol

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

#Puedo hacerlo mas amable creando un alias:

import extra.good.alpha as alp

print(alp.FunA())