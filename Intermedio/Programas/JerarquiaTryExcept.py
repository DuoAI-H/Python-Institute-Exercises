#Se puede usar solo ArithmeticError, pues es mas general
try:
    y = 1 / 0
#Si cambio los except de lugar, cambiara la salida
#Pues el problema pertenece a ambas excepciones
#Aunque es correcto tenerla asi como esta
#Pues ZeroDivisionError es mas concreto y esta dentro 
#de ArithmeticError, que es mas general.
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")

#Recordar: No poner excepciones mas generales antes que las concretas

#En caso de querer usar ambas excepciones:

    #except (ZeroDivisionError,ArithmeticError):