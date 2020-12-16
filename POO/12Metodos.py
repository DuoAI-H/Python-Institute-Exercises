# ejemplos de prueba aquíclass conClase:
class conClase:
    varia = 2
    def metodo(self):
        #Self se usa para las variables de clase
        print(self.varia, self.var)
        
    def otro(self):
        print("otro")

    def metodo2(self):
        print("método")
        #Self se usa para invocar otros metodos dentro de la clase.
        self.otro()

obj = conClase()
obj.var = 3
obj.metodo()
obj.otro()
obj.metodo2()