def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    #Se ejecuta solo si no hay una excepcion:
    else:
        print("Todo salió bien")
        return n
    #Se ejecuta siempre, sin importa lo que ha pasado antes:
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))