try:
    c = input('Ingrese una cadena: ')
    n = int(input('Valor (1 a 25): '))
    assert n>=1 and n<=25
except AssertionError:
    print('El valor no esta en el rango')
    exit()
except KeyboardInterrupt:
    print('El programa se ha detenido con exito')
    exit()
except:
    print('Un error inesperado ha ocurrido')
    exit()

#Sin espacios y todos son alfanumericos
if c.replace(" ","").isalnum() == True:
    respuesta = ''
    for char in c:
        #Descarta los numeros y los espacios
        if not char.isalpha():
            caracter = char
        else:
            code = ord(char) + n
            if  char.islower() and code>122 :
                #Rango Minus: 97-122
                code = (code - 122) + 96
            elif char.isupper() and code>90:
                #Rango Mayus: 65-90
                code = (code-90)+64
            caracter = chr(code)
        respuesta += caracter
    print(respuesta)
else: print('Ingresaste caracteres invalidos')


