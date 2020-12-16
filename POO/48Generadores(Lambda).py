#La funcion map() toma dos argumentos:
#1.Una funcion.
#2.Una lista:
    #2.1 Puede ser una tupla.
    #2.2 cualquier otro elemento iterador.
#Nota: la funcion map() puede aceptar mas de dos argumentos.
lista1 = [x for x in range(5)]
#map() es un iterador y por lo tanto, toca convertilo en una lista.
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()