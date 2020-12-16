lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)


###


listaUno = []

for ex in range(6):
    listaUno.append(10 ** ex)


listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)


###


lst = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lst)