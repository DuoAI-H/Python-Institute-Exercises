def addicion(ne):
    suma = 0
    for i in ne:
        suma += int(i)
    if suma>=10:
        suma = addicion(list(str(suma)))
    return suma

def obtener(ne):
    try:
        suma = addicion(ne)
    except:
        raise
    return suma

print('Ingrese su fecha de nacimiento: ')
n = input('DD MM AAAA ')

n = n.replace(" ","")

try:
    n = list(n)
    numero = obtener(n)
    print('Su numero de vida es: %d' % numero)
except TypeError:
    print("Error de tipado")
except:
    print("Error")