
#Busca letras en una cadena, en el mismo orden

def pos(palabra, cadena, pa='', a=0, i=0):
    pa = palabra[i]
    a = cadena.find(pa,a,len(cadena))
    if a != -1:
        if a != (len(cadena)-1):
             s = pos(palabra, cadena, pa, a, (i+1))
        else:
            return True
    else: 
        return False
    return s

print('Ingrese una palabra y una cadena')
palabra = input('Palabra: ')
cadena = input('Cadena: ')

#Faltan excepciones de entrada

#Usar find() y pos()
print(pos(palabra, cadena))