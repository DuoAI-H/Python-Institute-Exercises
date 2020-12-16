numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

###

numeros.insert(1,333)
print(numeros)

###

miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

###

miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1)

print(miLista)