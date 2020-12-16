#Capaces de producir una serie de valores y controlar
#el proceso de iteracion.
#A menudo se les llama iteradores.

class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

    #Metodo necesario en un iterador, debe devolver "self"
    #Siempre se instancia primero que next.
	def __iter__(self):
		print("__iter__")		
		return self
    #Metodo necesario en un iterador, el cual debe devolver
    #el siguiente valor.
	def __next__(self):
		print("__next__")				
		self.__i += 1
        #Si ya no hay mas valores para iterar, el metodo debera
        #lanzar la excepción "StopIteration"
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

#Secuencia for/in que invoca el metodo __next__
#El método __next__ se invoca once veces: las primeras diez 
#veces produce valores útiles, mientras que la ultima finaliza la iteración.
for i in Fib(10):
	print(i)