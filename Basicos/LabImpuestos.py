ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso<85528 and ingreso >0:
    impuesto=(0.18*ingreso)-556.2
elif ingreso<=0:
    impuesto = 0.0
else:
    impuesto=(14839.2+(0.32*(ingreso-85528)))

if impuesto>0:
    impuesto = round(impuesto, 0)
else :
    impuesto = 0
print("El impuesto es: ", impuesto, "pesos")
