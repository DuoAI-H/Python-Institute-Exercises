#raise genera una excepcion especificada

def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#Se usa con dos fines:

#Simular excepciones reales.
#Manejar parcialmente una excepcion y hacer que sea responsable de completarse.