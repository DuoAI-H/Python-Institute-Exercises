class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        #Aca se creo de esta manera pues se necesita poder acceder
        #a esta variable desde el exterior.

        #Si se hiciera:
            #self.varia = val 
        #crearia una instancia con el mismo nobre de la variable de clase.

        #Si se hiciera:
            #varia = val
        #crearia una variable local.
        ClaseEjemplo.varia = val

#Aca solo se imprime el valor del atributo.
#Se hizo sin crear el primer objeto de la clase.
print(ClaseEjemplo.varia)

objetoEjemplo = ClaseEjemplo(2)

#Diferencia variable __dict__ para clase y para objeto.

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)