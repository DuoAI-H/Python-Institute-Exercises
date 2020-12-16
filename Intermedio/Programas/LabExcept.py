def readint(prompt, min, max):
    try:
        n = input(prompt)-
        n = int(n)
        assert n<=max and n>=min
    except ValueError:
        print("Error : entrada incorrecta")
        exit()
    except AssertionError:
        print("Error: El valor no esta dentro del rango permitido")
        exit()
    except :
        print("Ha ocurrido un error inesperado")
        exit()
    return n

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
