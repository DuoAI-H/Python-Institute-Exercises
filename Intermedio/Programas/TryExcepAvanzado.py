try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    #Aca se accede con una excepcion denominada
    #KeyboardInterrupt
    #Si presiono Ctrl+C, detengo el programa
    print("Oh cielos, algo salio mal...")

print("THE END.")