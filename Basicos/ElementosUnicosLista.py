miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
respaldo = []
aux=0

for numero in miLista:
    if numero not in respaldo:
        respaldo.append(numero)
print("La lista solo con elementos únicos:")
print(respaldo)
