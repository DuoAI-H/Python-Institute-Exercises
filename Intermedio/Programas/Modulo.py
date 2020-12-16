#Importar un modulo:

    #import math

#Lo siguiente hace que el namespace y las variables que tengan el mismo nombre
#Puedan coexistir
#Este modulo se importa como namespace y toca nombrar las variables asi:

    #math.sin()
    #math.e()
    #math.pi()

#Importar un modulo y acceder a las entidades del namespace como variables:

    #from math import sin, e, pi

#Esto causa que podamos llamarlas por ese nombre y tambien que podamos editar su valor
#Hay que tener cuidado con esta propiedad de variacion
#Ahora es valido hacer el siguiente codigo usando el modulo math:

    #print(e)
    #print(pi)
    #print(sin(pi/2))

#Para importar todas las entidades por su nombre, se hace lo siguiente:
#Aunque se debe evitar esto, pues puede generar conflictos si no sabemos todos los nombres contenidos.

    #from math import *

#Si se decide cambiar el nombre del modulo, por otro que resulte mas a gusto o util, se hace esto:
#Donde el alias es el nuevo nombre a usar

    #import module as alias

#Asi mismo, si se necesita cambiar el nombre de la entidad, se hace lo siguiente:
#Recordando que los nombres originales de la entidad o del modulo, se vuelven innacesibles.

    #from module import entity as alias

#Para acceder a todos los nombres de un modulo (visualizarlos), se debe hacer lo siguiente:
#No funciona con from module
#Si el modulo tiene un alias, se debe usar el alias

    #import module
    #dir(module)