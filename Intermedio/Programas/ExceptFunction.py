#Si una excepcion se genera dentro de una funcion
#Se puede manejar dentro o fuera de la funcion

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")

#Si se quiere fuera de la funcion:

    """
    def badFun(n):
        return 1/n
    
    try:
        badFun(0)
    except AritmeticError:
        print("¿Que pasó? ¡Se lanzo una excepción!")
    print("FIN.")
    """