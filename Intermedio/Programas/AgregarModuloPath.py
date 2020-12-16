from sys import path

#Aca agrego el path pero Python no me crea la carpeta
path.append('c:\\Users\\lfpin\\OneDrive\\Documentos\\VS Code\\Python\\Python Institute\\Intermedio\\modules')

for p in path:
    print(p)

from module import sum1, prod1
#from module import *

zeroes =  [0 for i in range(5)]
ones = [1 for i in range(5)]

print(sum1(zeroes))
print(prod1(ones))