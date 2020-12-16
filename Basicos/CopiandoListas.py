# Copiando mal la lista
lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

#Otros ordenamientos

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1]
print(nuevaLista)

###

nuevaLista = miLista [-1:1]
print(nuevaLista)


#Desde el inicio

nuevaLista = miLista [:3]
print(nuevaLista)

#Hasta el final

nuevaLista = miLista [1:]
print(nuevaLista)

#Toda la lista

nuevaLista = miLista [:]
print(nuevaLista)