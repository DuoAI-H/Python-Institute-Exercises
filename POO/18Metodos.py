#Nota: La propiedad __module__ almacena el nombre del modulo que 
#contiene la definicion de la clase.
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)

#Cualquier modulo llamado __main__ (salida de la consola) en realiadad
#no es un modulo, sino es el archivo actualmente en ejecucion.