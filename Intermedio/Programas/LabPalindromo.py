try:
    word = input('Ingrese una cadena: ')
    assert word.strip() != ""
except AssertionError:
    print('Los espacios no son palindromos')
    exit()
except :
    print('Ha ocurrido un error')
    exit()

word = word.replace(" ","").upper()

a = True
lon = int(len(word)/2)

for i in range(lon):
    if word[i] != word[-(i+1)]:
        a = False

if a:
    print("Palindromo")
else:
    print("No palindromo")

#Otro metodo para invertir una cadena
    #word = ''.join(reversed(word))
    #word = word[::-1]
    #print(word)