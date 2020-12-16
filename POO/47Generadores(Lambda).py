def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

"""
def poli(x):
	return 2 * x**2 - 4 * x + 2
"""

#Utilizariamos esta si declaracemos la funcion, pero
#esta es una funcion de un solo uso, para evitar eso:

    #imprimirfuncion([x for x in range(-2, 3)], poli)

#definimos una funcion lambda

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)