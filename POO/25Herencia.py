#Nota: el operador -is- verifica si dos variables (en este caso,
# objetos) se refieren al mismo objeto.

#Nota: las variables no almacen objetos en si, sino solo los identificadores
#que apuntan a la memoria interna de Python.

class ClaseMuestra:
    def __init__(self, val):
        self.val = val

ob1 = ClaseMuestra(0)
ob2 = ClaseMuestra(2)
#Aca no se copia el objeto, solo su identificador.
ob3 = ob1
#El identificador hace que la variable se guarda en ob3 y ob1
#Y que ob3 sea igual a ob1 y que ob1 sea igual a ob3
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1 is ob3)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary tenía un "
str2 = "Mary tenía un corderito"
str1 += "corderito"

#Los valores son iguales pero no son los mismos objetos
print(str1 == str2, str1 is str2)