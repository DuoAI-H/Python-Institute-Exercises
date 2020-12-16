class MiClase:
    pass

#Creamos el objeto.
obj = MiClase()
#Creamos caracteristicas propias para este objeto.
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

#La funcion obtiene un objeto de cualquier clase.
#Despues escanea su contenido para encontrar el atributo 'i'.
#Incrementa ese atributo en 1.
def incIntsI(obj):
    #Accedemos a las propiedades y a sus llaves (nombres).
    for name in obj.__dict__.keys():
        #Si el nombre empieza con 'i'
        if name.startswith('i'):
            #Tomamos el valor del parametro con la funcion getattr.
            #Esta nos pide como entradas el objeto y el nombre de la variable.
            val = getattr(obj, name)
            #Comprueba si el valor es de tipo entero con la funcion isinstance.
            if isinstance(val, int):
                #Con la funcion setattr le asignamos un valor al atributo, incrementandolo en 1.
                #La funcion nos pide como argumentos el objeto, el nombre del argumento y el valor a asignar.
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)