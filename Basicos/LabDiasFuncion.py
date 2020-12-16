#True = año bisiesto
#False = año normal

De31 = [1,3,5,7,8,10,12]

def isYearLeap(año):
    if año>=1582:
        if año%4 != 0:
            return (0)
        elif año%100 != 0:
            return (1)
        elif año%400 != 0:
            return (0)
        else:
            return (1)

#Devuelve dias del mes por año especifico
def daysInMonth(year, month):
    bisiesto = isYearLeap(year)
    if month in De31:
        return (31)
    elif month == 2:
        if bisiesto:
            return(29)
        else:
            return(28)
    elif month not in De31:
        return (30)
    else:
        return (None)

#Me dice el dia de la semana
def QueDia(dia):
    dia = dia%7
    if dia == 0: fecha = "Viernes"
    elif dia == 1: fecha = "Sabado"
    elif dia == 2: fecha = "Domingo"
    elif dia == 3: fecha = "Lunes"
    elif dia == 4: fecha = "Martes"
    elif dia == 5: fecha = "Miercoles"
    else: fecha = "Jueves"
    return (fecha)

#Calcula el dia segun la fecha
def daysFecha(day,month, year):
    bis=0
    years = (year-1582)
    for i in range(1582,year):
        if isYearLeap(i):
            bis +=1
    days = (bis*366)+((years-bis)*365) #Dias por año
    for j in range(1, month):
        days = daysInMonth(year, j) + days
    days = days + day - 1
    dia = QueDia(days)
    return(dia)
        

#Fechas de testeo
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testDays = [4,12,17,28]
testResults = ["Domingo", "Sabado", "Domingo", "Sabado"]

#Testeo
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    da = testDays[i]
    print(da, mo, yr,"-> ", end="")
    result = daysFecha(da, mo, yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")


