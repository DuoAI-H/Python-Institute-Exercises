bloques = int(input("Ingrese el numero de bloques: "))
i,j=1,0
while True:
    j+=i
    if j>bloques:
        break
    i+=1
print("La altura de la piramide es: ",i-1)
    