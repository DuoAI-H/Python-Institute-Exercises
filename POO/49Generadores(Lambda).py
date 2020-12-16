#Recibe los mismos argumentos que map()
#Devuelve los elementos que regresen True del primer argumento.
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)