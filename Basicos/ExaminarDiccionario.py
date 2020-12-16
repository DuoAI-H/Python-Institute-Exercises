dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

#Imprimir llaves
for key in dict.keys():
    print(key, "->", dict[key])

#Ordenar llaves
for key in sorted(dict.keys()):
    print(key, "->", dict[key])

#Lista de tuplas
for spanish, french in dict.items():
    print(spanish, "->", french)

#Lista de valores
for french in dict.values():
    print(french)

#Cambiar un valor
dict['gato'] = 'minou'
print(dict)

#Agregar llaves y valores
dict['cisne'] = 'cygne'
print(dict)

#Otro metodo para agregar llaves
dict.update({"pato" : "canard"})
print(dict)

#Elminar clave
del dict['perro']
print(dict)

#Eliminar el ultimo elemento del diccionario
dict.popitem()
print(dict)