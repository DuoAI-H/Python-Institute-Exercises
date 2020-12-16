año = int(input("Introduzca un año:"))

if año>=1582:
    if año%4 != 0:
        print("Año común")
    elif año%100 != 0:
        print("Año bisiesto")
    elif año%400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")
else:
    print("No dentro del período del calendario")
