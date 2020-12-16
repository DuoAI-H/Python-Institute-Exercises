numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

print(numeros[0]) # accediendo al primer elemento de la lista.

del numeros[0] #Instrucción, no función
print(len(numeros)) #Reduce en 1 la longitud y elimina el dato
print(numeros) 

print(numeros[-1]) #Ultimo de la lista
print(numeros[-2]) #Penultimo de la lista