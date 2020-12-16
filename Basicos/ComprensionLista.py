cuadrados = [x**2 for x in range(10)]
print(cuadrados)

###

dos = [2**i for i in range(8)]
print(dos)

###

probabilidades = [x for x in cuadrados if x%2 != 0]
print(probabilidades)