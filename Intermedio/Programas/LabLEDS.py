#Variables
nV =[]

L0 = ('### ','# # ','# # ','# # ','### ')
L1 = ('  # ','  # ','  # ','  # ','  # ')
L2 = ('### ','  # ','### ','#   ','### ')
L3 = ('### ','  # ','### ','  # ','### ')
L4 = ('# # ','# # ','### ','  # ','  # ')
L5 = ('### ','#   ','### ','  # ','### ')
L6 = ('### ','#   ','### ','# # ','### ')
L7 = ('### ','  # ','  # ','  # ','  # ')
L8 = ('### ','# # ','### ','# # ','### ')
L9 = ('### ','# # ','### ','  # ','### ')

#Funciones
def ordNumeros(n):
    for i in range(len(n)):
        if n[i] == 0:nV[i] = L0
        elif n[i]==1:nV[i] = L1
        elif n[i]==2:nV[i] = L2
        elif n[i]==3:nV[i] = L3
        elif n[i]==4:nV[i] = L4
        elif n[i]==5:nV[i] = L5
        elif n[i]==6:nV[i] = L6
        elif n[i]==7:nV[i] = L7
        elif n[i]==8:nV[i] = L8
        else :nV[i] = L9

def conNumeros(nV):
    respuesta = ['' for i in range(5)]
    for z in range(5):
        for i in range(len(nV)):
            respuesta[z] += nV[i][z]
        respuesta[z] += '\n'
    return respuesta


#Entrada datos
while True:
    try:
        n = input("Ingrese un numero entero: ")
        if n == "exit" or n=="Exit":
            break
        n = int(n)
        assert n>0 or n<9
        nV.append(n)
    except AssertionError:
        print(" Error: El valor no esta dentro del rango permitido")
        exit()
    except KeyboardInterrupt:
        print(" Programa detenido por interrupcion del teclado")
        exit()
    except:
        print(" Error")
        exit()

print(nV)

ordNumeros(nV)

R = conNumeros(nV)

print(''.join(R))

#Numeros = [L0, L1, L2, L3, L4, L5, L6, L7, L8, L9]
"""
for i in Numeros:
    print(''.join(i))
    print()
"""