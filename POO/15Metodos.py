#Nota: Un nombre con __ al inicio, esta parcialmente oculto.
#A esto se le conoce como encapsulamiento y da privacidad al metodo o variable.
class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto()