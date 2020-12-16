def isPrime(num):
    if num % 2 == 0 and num!=2: return(0)
    elif num % 3 == 0 and num!=3: return(0)
    elif num % 5 == 0 and num!=5: return(0)
    elif (num ** 0.5)%1 == 0: return(0)
    else:
        for i in range(7,int(num**0.5)):
            if num%i == 0:
                return(0)
        return(1)

for i in range(1, 100):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()