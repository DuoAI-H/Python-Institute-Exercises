#Nota: la situacion en la cual la subclase puede modificar
#el comportamiento de su superclase, se llama polimorfismo.
class Uno:
    def hazlo(self):
        print("hazlo de Uno")

    def haz_algo(self):
        self.hazlo()

class Dos(Uno):
    def hazlo(self):
        print("hazlo de Dos")

uno = Uno()
dos = Dos()

uno.haz_algo()
dos.haz_algo()