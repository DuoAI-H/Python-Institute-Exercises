#Nota: cierres es una tecnica que permite almacenar
#valores a pesar de que el contexto en el que se crearon
#ya no existe.

def exterior(par):
	loc = par
    #interior() solo se puede invotar dentro de exterior().
	def interior():
		return loc
    #devuelve una copia de la funcion interior()
	return interior

var = 1
fun = exterior(var)
print(fun())