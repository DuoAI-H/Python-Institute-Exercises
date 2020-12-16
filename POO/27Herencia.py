# Probando propiedades: variables de clase
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2


#La variables de clase se heredan y son 
#accesibles desde la subclase.
obj = Sub()

print(obj.subVar)
print(obj.supVar)