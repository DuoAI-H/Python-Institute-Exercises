#Nota: "yield" proporciona el valor de la expresion especificada
#despues de la palabra clave reservada yield, al igual que return,
#pero no pierde el estado de la función.

#Todos los valores de las variables estan congelados y esperan la
#proxima invocación, cuando se reanuda la ejecución.

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)