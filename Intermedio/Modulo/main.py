from module import sum1, prod1

#Esto no se debe hacer, por integridad del modulo
#print(module.__counter)

zeroes =  [0 for i in range(5)]
ones = [1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))