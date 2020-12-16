#Los corchetes hacen una comprensión
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
#Los parentesis hacen un generador
genr = (1 if x % 2 == 0 else 0 for x in range(10))

#En el primer bucle, la lista se crea y se itera como un todo,
#en realidad existe cuando se ejecuta el bucle.
for v in lst:
    print(v, end=" ")
print()

#En el segundo bucle, no hay ninguna lista, solo hay valores subsecuentes
#producidos por el generador, uno por uno.
for v in genr:
    print(v, end=" ")
print()

#Es por esto que si usamos la funcion len() sobre la lst, nos dar aun resultado
#pero si la usamos sobre el generador, nos dara una excepción.