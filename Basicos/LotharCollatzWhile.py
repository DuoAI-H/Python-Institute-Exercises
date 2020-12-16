c0 = int(input("Ingrese un numero: "))
paso=0
while c0!=1:
    if c0%2 == 0:
        c0 = c0/2
    else:
        c0 = 3*c0+1
    paso+=1
    print(int(c0))
print("Pasos: ",paso)