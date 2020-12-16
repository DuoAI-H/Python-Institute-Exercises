miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>

#Convertir una tupla a una lista
tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>