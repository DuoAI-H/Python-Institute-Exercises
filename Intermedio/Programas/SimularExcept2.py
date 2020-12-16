#Esta variante puede ser utilizada solamente dentro de la rama
#Except:
#Usarla en otro caso causaria un error

def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        #Sirve para generar la misma excepcion
        #que maneja actualmente.
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#Esto sirve para distribuir el manejo de excepciones
#entre diferentes partes del codigo.