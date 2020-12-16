#Demostrando la funcion ord()

#Devuelve el valor del punto de codigo
#para un caracter especifido ASCII/UNICODE

ch1 ='a'
ch2 = ' ' #espacio
ch3 = 'α'
ch4 = 'ę'

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))
print(ord(ch4))

#Si se conoce el punto de codigo, se puede devolver el caracter asociado

print(chr(97))
print(chr(945))