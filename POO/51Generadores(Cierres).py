def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)
for i in range(5):
    #Aca es donde se declaran los valores de p
	print(i, fsqr(i), fcub(i))