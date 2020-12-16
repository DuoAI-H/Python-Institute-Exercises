#Nota: cuando un objeto deba ser presentado como una cadena,
#Python buscara el metodo __str__().
#El metodo por defecto devuelve una cadena del siguiente estilo:
    #<__main__.Estrella object at 0x0311B418>
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia
    #El nombre por default se puede cambiar creando nuestro propio nombre,
    #cuando definimos el metodo en nuestra clase.
    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)