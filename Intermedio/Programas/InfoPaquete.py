#Un paquete es un conjunto de carpetas ordenadas en arbol (jerarquia)
#Estas carpetas contienen modulos, que a vez, contienen funciones
#Los paquetes no se llaman como los modulos, para eso se usa otro archivo contenido en la carpeta inicial.

#El archivo debe estar en la carpeta inicial del nombre del paquete y se debe llamar:

    #__init__.py

#Este archivo tambien puede ir en otras carpetas si se desea un tratamiento de inicializacion especial

#Se puede inicializar un paquete de las siguientes maneras:

    #path.append('c:\\Users\\lfpin\\OneDrive\\Documentos\\VS Code\\Python\\Python Institute\\Intermedio\\Paquetes')
    #path.insert(0,'Paquetes')
    #path.append('Paquetes')

#Antes se tiene que llamar al modulo sys de la siguiente manera:

    #from sys import path